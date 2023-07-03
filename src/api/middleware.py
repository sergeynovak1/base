from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest, HttpResponse
from .models import APIRequestLog


class APIRequestLogMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        if request.path.startswith('/api'):
            log = APIRequestLog()
            log.client_ip = request.META.get('REMOTE_ADDR')
            log.request_url = request.path
            log.request_headers = dict(request.headers)
            log.request_body = request.body.decode('utf-8')
            log.request_method = request.method
            log.created_at = datetime.now()
            log.save()

            parent_log_id = request.META.get('HTTP_PARENT_LOG_ID')
            if parent_log_id:
                log.parent_log_id = parent_log_id
                log.save()

            request.api_log_id = log.id

    def process_response(self, request: HttpRequest, response: HttpResponse):
        if request.path.startswith('/api') and hasattr(request, 'api_log_id'):
            log_id = request.api_log_id

            log = APIRequestLog.objects.get(pk=log_id)
            log.response_status_code = response.status_code
            log.response_body = response.content.decode('utf-8')
            log.save()

        return response

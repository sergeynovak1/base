from django.db import models

from users.models import User


class APIRequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    client_ip = models.CharField(max_length=255)
    parent_log_id = models.IntegerField(blank=True, null=True)
    request_url = models.CharField(max_length=255)
    request_headers = models.JSONField()
    request_body = models.TextField()
    request_method = models.CharField(max_length=10)
    response_status_code = models.IntegerField(blank=True, null=True)
    response_body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

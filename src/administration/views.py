from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .enums import Method
from api.models import APIRequestLog


@user_passes_test(lambda u: u.is_superuser)
def logs_list(request):
    method_filter = request.GET.get('method')
    search_query = request.GET.get('search')
    logs = APIRequestLog.objects.all()

    if search_query:
        logs = logs.filter(Q(client_ip__icontains=search_query))

    if method_filter:
        logs = logs.filter(request_method=method_filter)

    return render(request, 'log_list.html', {'logs': logs, 'method_filter': method_filter, 'methods': Method.choices, 'search_query': search_query})


@user_passes_test(lambda u: u.is_superuser)
def log_card(request, log_id):
    log = get_object_or_404(APIRequestLog, id=log_id)
    return render(request, 'log_card.html', {'log': log})
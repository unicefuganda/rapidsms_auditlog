import os
from django.shortcuts import render, redirect
from auditlog.models import Auditlog
from auditlog.utils import audit_log
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

def auditlog_dashboard(request):
    #log_dict = {'request':request, 'action':'login', 'logtype':'system', 'detail':'User Logged In'}
    #audit_log(log_dict)
    logs = Auditlog.objects.all().order_by('-created')
    paginator = Paginator(logs, 10)
    page = request.GET.get('page')
    page = int(page) if page else 1

    try:
        logs = paginator.page(page)
    except PageNotAnInteger:
        logs = paginator.page(1)
    except EmptyPage:
        logs = paginator.page(paginator.num_pages)

    return render(request, 'auditlog/index.html', {'logs':logs})

def auditlog_logs(request):

    s = os.popen("tail -n 20 %s" % getattr(settings, 'AUDITLOG_LOGFILE', '/var/log/rapidsms/auditlog.log'))
    logs = s.readlines()
    return render(request, 'auditlog/logs.html', {'logs':logs})


from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import patterns, url
from rapidsms_auditlog.auditlog.views import *

urlpatterns = patterns ('',
                url(r'^$', auditlog_dashboard, name="auditlog_dashboard"),
                url(r'^logs/$', auditlog_logs, name="logs"),
)

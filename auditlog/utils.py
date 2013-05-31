import logging
from auditlog.models import Auditlog
from django.conf import settings

logging.basicConfig(level=logging.INFO,
        format='%(asctime)s [%(process)d] %(levelname)-4s:  %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=getattr(settings, 'AUDITLOG_LOGFILE', '/var/log/rapidsms/auditlog.log'),
        filemode='a')

def audit_log(log_dict):
    """
        This functions logs the event to Auditlog model
        and the logfile
        the argument log_dict is a dictionary of the following form
        {'request': request, 'logtype': logtype, 'action': '', 'detail': '', 'old_value':''}
    """
    request = log_dict.get('request','')
    if not request:
        return
    user = request.user
    log_dict['old_value'] = log_dict.get('old_value', '')
    log_dict['user'] = "%s: %s" % (user.id, user.username)
    log_dict['remote_addr'] = request.environ['REMOTE_ADDR']
    log_obj = Auditlog.objects.create(user=log_dict['user'],
            remote_addr = log_dict['remote_addr'],
            logtype = log_dict['logtype'],
            action = log_dict['action'],
            detail = log_dict['detail'],
            old_value = log_dict['old_value'])
    logging.info("[user: %(user)s] [logtype: %(logtype)s] [action: %(action)s] [detail: %(detail)s]" % log_dict)
    return



from django.db import models
from datetime import datetime

# Create your models here.
class Auditlog(models.Model):
    LOGTYPE_CHOICES = (
        ('System', 'system'),
        ('Anonymous Report', 'anonymous'),
        ('XForm Report', 'xform'),
        ('Other', 'other'),
    )
    ACTION_CHOICES = (
        ('Login', 'login'),
        ('Logout', 'logout'),
        ('Edit', 'edit'),
        ('Delete', 'delete'),
        ('SendSMS', 'sendsms'),
        ('SendPoll', 'sendpoll'),
    )
    created = models.DateTimeField(default=datetime.now())
    # remote_addr = models.GenericIPAddressField(default='127.0.0.1')
    remote_addr = models.TextField(default='127.0.0.1')
    user = models.TextField(default='')  # takes user_id and name e.g '100:sam'
    logtype = models.CharField(max_length=32, default='system', choices=LOGTYPE_CHOICES)
    action = models.CharField(max_length=32, choices=ACTION_CHOICES)
    detail = models.TextField(default='')
    old_value = models.TextField(default='', null=True, blank=True)
    class Meta:
        db_table = 'auditlog'

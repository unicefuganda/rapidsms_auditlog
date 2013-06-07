# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Auditlog'
        db.create_table('auditlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 6, 8, 0, 0))),
            ('remote_addr', self.gf('django.db.models.fields.TextField')(default='127.0.0.1')),
            ('user', self.gf('django.db.models.fields.TextField')(default='')),
            ('logtype', self.gf('django.db.models.fields.CharField')(default='system', max_length=32)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('detail', self.gf('django.db.models.fields.TextField')(default='')),
            ('old_value', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal('auditlog', ['Auditlog'])


    def backwards(self, orm):
        # Deleting model 'Auditlog'
        db.delete_table('auditlog')


    models = {
        'auditlog.auditlog': {
            'Meta': {'object_name': 'Auditlog', 'db_table': "'auditlog'"},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 8, 0, 0)'}),
            'detail': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logtype': ('django.db.models.fields.CharField', [], {'default': "'system'", 'max_length': '32'}),
            'old_value': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'remote_addr': ('django.db.models.fields.TextField', [], {'default': "'127.0.0.1'"}),
            'user': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['auditlog']
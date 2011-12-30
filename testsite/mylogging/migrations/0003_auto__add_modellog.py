# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Modellog'
        db.create_table('mylogging_modellog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('inst_pk', self.gf('django.db.models.fields.IntegerField')()),
            ('app', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('mylogging', ['Modellog'])


    def backwards(self, orm):
        
        # Deleting model 'Modellog'
        db.delete_table('mylogging_modellog')


    models = {
        'mylogging.modellog': {
            'Meta': {'object_name': 'Modellog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'app': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inst_pk': ('django.db.models.fields.IntegerField', [], {}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'mylogging.request': {
            'Meta': {'object_name': 'Request'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'get': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['mylogging']

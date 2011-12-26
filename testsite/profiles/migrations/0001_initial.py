# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Profile'
        db.create_table('profiles_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('birth', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('profiles', ['Profile'])

        # Adding model 'Contact'
        db.create_table('profiles_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Profile'])),
            ('mean', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('data', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('profiles', ['Contact'])


    def backwards(self, orm):
        
        # Deleting model 'Profile'
        db.delete_table('profiles_profile')

        # Deleting model 'Contact'
        db.delete_table('profiles_contact')


    models = {
        'profiles.contact': {
            'Meta': {'object_name': 'Contact'},
            'data': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mean': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Profile']"})
        },
        'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['profiles']

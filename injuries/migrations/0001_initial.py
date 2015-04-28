# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Treatment'
        db.create_table(u'injuries_treatment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'injuries', ['Treatment'])

        # Adding model 'Exercise'
        db.create_table(u'injuries_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'injuries', ['Exercise'])

        # Adding model 'Injury'
        db.create_table(u'injuries_injury', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('x_axis', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('y_axis', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'injuries', ['Injury'])

        # Adding M2M table for field exercises on 'Injury'
        m2m_table_name = db.shorten_name(u'injuries_injury_exercises')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('injury', models.ForeignKey(orm[u'injuries.injury'], null=False)),
            ('exercise', models.ForeignKey(orm[u'injuries.exercise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['injury_id', 'exercise_id'])


    def backwards(self, orm):
        # Deleting model 'Treatment'
        db.delete_table(u'injuries_treatment')

        # Deleting model 'Exercise'
        db.delete_table(u'injuries_exercise')

        # Deleting model 'Injury'
        db.delete_table(u'injuries_injury')

        # Removing M2M table for field exercises on 'Injury'
        db.delete_table(db.shorten_name(u'injuries_injury_exercises'))


    models = {
        u'injuries.exercise': {
            'Meta': {'object_name': 'Exercise'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'injuries.injury': {
            'Meta': {'object_name': 'Injury'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'exercises': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['injuries.Exercise']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'x_axis': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'y_axis': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'injuries.treatment': {
            'Meta': {'object_name': 'Treatment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['injuries']
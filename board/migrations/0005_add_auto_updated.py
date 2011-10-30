# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'BoardMember.updated'
        db.add_column('board_boardmember', 'updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 10, 30, 9, 35, 27, 271000), auto_now=True, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'BoardMember.updated'
        db.delete_column('board_boardmember', 'updated')
    
    
    models = {
        'board.boardmember': {
            'Meta': {'object_name': 'BoardMember'},
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'forename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 10, 30, 9, 35, 27, 271000)', 'auto_now': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['board']

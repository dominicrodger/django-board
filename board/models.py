from sorl.thumbnail import ImageField, get_thumbnail
from django.conf import settings
from django.db import models
import os

class BoardMember(models.Model):
    title = models.CharField(max_length = 100, help_text = u'The board member\'s title (Mr, Mrs, Dr, etc.)')
    forename = models.CharField(max_length = 100, help_text = u'The board member\'s forename')
    surname = models.CharField(max_length = 100, help_text = u'The board member\'s surname')
    position = models.CharField(max_length = 255, blank = True, null = True, help_text = u'Their position on the board')
    biography = models.TextField(blank = True, null = True, help_text = u'A brief biography of the board member')
    email = models.EmailField(blank = True, null = True)
    image = ImageField(upload_to = 'board', blank = True, null = True)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.title, self.forename, self.surname)

    def admin_thumbnail(self):
        im = get_thumbnail(self.image, '100x100', crop='center', quality=99)
        return u'<img src="{0}" />'.format(im.url)
    admin_thumbnail.short_description = 'Image'
    admin_thumbnail.allow_tags = True

    class Meta:
        ordering = ('surname', 'forename',)

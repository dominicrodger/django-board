from sorl.thumbnail import ImageField, get_thumbnail
from datetime import datetime
from django.db import models


class BoardMember(models.Model):
    title = models.CharField(max_length=100,
                             help_text=('The board member\'s '
                                        'title (Mr, Mrs, Dr, etc.)'),
                             blank=True, null=True)
    forename = models.CharField(max_length=100,
                                help_text=u'The board member\'s forename')
    surname = models.CharField(max_length=100,
                               help_text=u'The board member\'s surname')
    position = models.CharField(max_length=255, blank=True, null=True,
                                help_text=u'Their position on the board')
    biography = models.TextField(blank=True, null=True,
                                 help_text=('A brief biography of '
                                            'the board member'))
    email = models.EmailField(blank=True, null=True)
    image = ImageField(upload_to='board', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, default=datetime.now(),
                                   verbose_name=u'Last Updated')

    def __unicode__(self):
        if self.title:
            return u'{0} {1} {2}'.format(self.title,
                                         self.forename,
                                         self.surname)
        return u'{0} {1}'.format(self.forename, self.surname)

    def name(self):
        return self.__unicode__()
    name.short_description = u'Name'
    name.admin_order_field = 'surname'

    def admin_thumbnail(self):
        if not self.image:
            return u'(None)'
        im = get_thumbnail(self.image, '100x100', crop='center', quality=99)
        return u'<img src="{0}" />'.format(im.url)
    admin_thumbnail.short_description = 'Image'
    admin_thumbnail.allow_tags = True

    class Meta:
        ordering = ('surname', 'forename',)

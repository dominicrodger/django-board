from django.db import models

class BoardMember(models.Model):
    title = models.CharField(max_length = 100, help_text = u'The board member\'s title (Mr, Mrs, Dr, etc.)')
    forename = models.CharField(max_length = 100, help_text = u'The board member\'s forename')
    surname = models.CharField(max_length = 100, help_text = u'The board member\'s surname')
    position = models.CharField(max_length = 255, blank = True, null = True, help_text = u'Their position on the board')
    biography = models.TextField(blank = True, null = True, help_text = u'A brief biography of the board member')
    email = models.EmailField(blank = True, null = True)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.title, self.forename, self.surname)

    class Meta:
        ordering = ('surname', 'forename',)

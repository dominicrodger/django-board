from django.contrib import admin
from board.models import BoardMember

class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('forename', 'surname', 'position', 'email',)
    search_fields = ('forename', 'surname', 'position', 'email', 'biography',)
admin.site.register(BoardMember, BoardMemberAdmin)
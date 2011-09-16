from django.contrib import admin
from board.models import BoardMember
from sorl.thumbnail.admin import AdminImageMixin

class BoardMemberAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('forename', 'surname', 'admin_thumbnail', 'position', 'email',)
    search_fields = ('forename', 'surname', 'position', 'email', 'biography',)
admin.site.register(BoardMember, BoardMemberAdmin)
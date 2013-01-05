from django.contrib import admin
from board.models import BoardMember
from sorl.thumbnail.admin import AdminImageMixin


class BoardMemberAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'admin_thumbnail', 'position', 'email', 'updated')
    search_fields = ('forename', 'surname', 'position', 'email', 'biography',)

admin.site.register(BoardMember, BoardMemberAdmin)

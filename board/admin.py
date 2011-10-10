from django.contrib import admin
from board.models import BoardMember
from sorl.thumbnail.admin import AdminImageMixin
from tinymce.widgets import TinyMCE

class BoardMemberAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'admin_thumbnail', 'position', 'email',)
    search_fields = ('forename', 'surname', 'position', 'email', 'biography',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('biography',):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
            ))
        return super(BoardMemberAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(BoardMember, BoardMemberAdmin)

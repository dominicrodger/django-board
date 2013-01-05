from board.models import BoardMember
from django import template


register = template.Library()


@register.assignment_tag
def board_members():
    return BoardMember.objects.all()

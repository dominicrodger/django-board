from django.views.generic.list import ListView
from board.models import BoardMember

class BoardListView(ListView):
    queryset = BoardMember.objects.all()
    context_object_name = 'board_members'

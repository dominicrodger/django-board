from django.conf.urls.defaults import *
from board.views import BoardListView

urlpatterns = patterns('',
    url(r'^$', BoardListView.as_view(), name='board_index'),
)
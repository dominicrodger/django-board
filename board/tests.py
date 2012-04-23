from django.core.urlresolvers import reverse
from django.test import TestCase
from board.models import BoardMember

class BoardMemberTestCase(TestCase):
    fixtures = ['test_board.json',]

    def setUp(self):
        self.edgar = BoardMember.objects.get(pk = 1)
        self.guido = BoardMember.objects.get(pk = 2)

    def testUnicode(self):
        self.assertEqual(self.edgar.__unicode__(), u'Prof Edgar Dijkstra')
        self.assertEqual(self.guido.__unicode__(), u'Guido van Rossum')
        self.assertEqual(self.edgar.name(), u'Prof Edgar Dijkstra')
        self.assertEqual(self.guido.name(), u'Guido van Rossum')

    def testBoardList(self):
        response = self.client.get(reverse('board_index',))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['board_members']), [self.edgar, self.guido,])

        # E-mail addresses should be private
        self.assertNotContains(response, 'guido@pythoneers.org')

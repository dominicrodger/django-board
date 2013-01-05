from django.core.urlresolvers import reverse
from django.test import TestCase
from board.models import BoardMember


class BoardMemberTestCase(TestCase):
    def setUp(self):
        self.edgar, is_new = BoardMember.objects.get_or_create(title="Prof",
                                                       forename="Edgar",
                                                       surname="Dijkstra")
        self.guido, is_new = BoardMember.objects.get_or_create(forename="Guido",
                                                       surname="van Rossum",
                                                       email="guido@pythoneers.org")

    def testUnicode(self):
        self.assertEqual(self.edgar.__unicode__(), u'Prof Edgar Dijkstra')
        self.assertEqual(self.guido.__unicode__(), u'Guido van Rossum')
        self.assertEqual(self.edgar.name(), u'Prof Edgar Dijkstra')
        self.assertEqual(self.guido.name(), u'Guido van Rossum')

    def testBoardList(self):
        response = self.client.get(reverse('board_index',))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['board_members']),
                         [self.edgar, self.guido, ])

        # E-mail addresses should be private
        self.assertNotContains(response, 'guido@pythoneers.org')

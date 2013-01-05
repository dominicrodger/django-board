from django.core.urlresolvers import reverse
from django.test import TestCase
from board.models import BoardMember


class BoardMemberTestCase(TestCase):
    def test_unicode(self):
        edgar = BoardMember(title="Prof",
                            forename="Edgar",
                            surname="Dijkstra")
        self.assertEqual(unicode(edgar), u'Prof Edgar Dijkstra')
        edgar.title = ""
        self.assertEqual(unicode(edgar), u'Edgar Dijkstra')

    def test_name(self):
        edgar = BoardMember(title="Prof",
                            forename="Edgar",
                            surname="Dijkstra")
        self.assertEqual(edgar.name(), u'Prof Edgar Dijkstra')
        edgar.title = ""
        self.assertEqual(edgar.name(), u'Edgar Dijkstra')

    def test_board_list_view(self):
        edgar = BoardMember.objects.create(title="Prof",
                                           forename="Edgar",
                                           surname="Dijkstra")
        guido = BoardMember.objects.create(forename="Guido",
                                           surname="van Rossum",
                                           email="guido@pythoneers.org")

        response = self.client.get(reverse('board_index',))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['board_members']),
                         [edgar, guido, ])

        # E-mail addresses should be private
        self.assertNotContains(response, 'guido@pythoneers.org')

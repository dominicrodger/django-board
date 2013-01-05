from django.template import Context, Template
from django.test import TestCase
from board.models import BoardMember
import factory


def render_template(input):
    t = Template("{% load board_tags %}" + input)
    c = Context()
    return t.render(c).strip()


class BoardMemberFactory(factory.Factory):
    title = "Prof"
    forename = "Edgar"
    surname = "Dijkstra"


class BoardMemberTestCase(TestCase):
    def test_unicode(self):
        edgar = BoardMemberFactory()
        self.assertEqual(unicode(edgar), u'Prof Edgar Dijkstra')
        edgar.title = ""
        self.assertEqual(unicode(edgar), u'Edgar Dijkstra')

    def test_name(self):
        edgar = BoardMemberFactory()
        self.assertEqual(edgar.name(), u'Prof Edgar Dijkstra')
        edgar.title = ""
        self.assertEqual(edgar.name(), u'Edgar Dijkstra')

    def test_board_assignment_tag(self):
        edgar = BoardMemberFactory.create()
        guido = BoardMemberFactory.create(title="",
                                          forename="Guido",
                                          surname="van Rossum",
                                          email="guido@pythoneers.org")

        t = ("{% board_members as members %}"
             "{% for member in members %}"
             "{{ member.name }}"
             "{% if not forloop.last %}; {% endif %}"
             "{% endfor %}")

        self.assertEqual("Prof Edgar Dijkstra; Guido van Rossum",
                         render_template(t))

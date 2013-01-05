django-board
============

A pluggable Django app for managing board members of an
organisation. Board members have titles, mini-biographies, and photos.

Installation is simple::

    pip install django-board

Getting started
---------------

Add the following to your ``INSTALLED_APPS``:

 * ``sorl.thumbnail`` (if not already present);
 * ``board``.

Sync database changes, using::

    python manage.py syncdb

django-board ships with no views, templates or URLs. To include a list
of board members in a template, use the template tag ``board_members``::


    {% load board_tags %}
    {% board_members as members %}

    {% if members %}
    <ul>
      {% for member in members %}
      <li>{{ member.name }}</li>
      {% endfor %}
    </ul>
    {% endif %}


Running the tests
-----------------

You can run the test suite using::

    python manage.py test board

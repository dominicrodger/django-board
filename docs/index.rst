Welcome to django-board's documentation!
========================================

A pluggable Django app for managing board members of an
organisation. Board members have titles, mini-biographies, and photos.

You can install this directly from GitHub with pip::

    pip install django-board

Getting started
---------------

Add the following to your ``INSTALLED_APPS``:

 * ``sorl.thumbnail`` (if not already present);
 * ``board``.

Sync database changes, using::

    python manage.py syncdb

You can run the test suite using::

    python manage.py test board

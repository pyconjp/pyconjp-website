=====================
PyCon JP サイト！
=====================

ローカル開発
----------------------

* virtualenvを作成::

    $ virtualenv env/pycon
    $ . env/pycon/bin/activate

* Install the requirements for running and testing locally::

    $ pip install -r requirements/dev.txt

* Copy ``pycon/settings/local.py-example`` to ``pycon/settings/local.py``.
* Edit ``pycon/settings/local.py`` according to the comments. Note that you
  `will` have to edit it; by default everything there is commented out.

* Setup the database::

    $ ./load_fixtures.sh

* Create a user account::

    $ ./manage.py createsuperuser

* If you have ssh access to the staging server, copy the database and media::

    $ fab staging get_db_dump:pycon2014
    $ fab staging get_media

  Change ``pycon2014`` in that first command to the name of your local database.

* Run local server::

    python manage.py runserver



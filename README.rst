=====================
PyCon JP サイト！
=====================

運用フロー
----------------------

* `各ブランチの役割 <https://github.com/pyconjp/pyconjp-website/wiki/%E5%90%84%E3%83%96%E3%83%A9%E3%83%B3%E3%83%81%E3%81%AE%E5%BD%B9%E5%89%B2>`_
* `運用フロー <https://github.com/pyconjp/pyconjp-website/wiki/%E9%81%8B%E7%94%A8%E3%83%95%E3%83%AD%E3%83%BC%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6>`_

ローカル開発
----------------------

* Pythonのバージョン::
    Python 2系
    2.7.11推奨

* virtualenvを作成, make::

    $ virtualenv env/pycon
    $ . env/pycon/bin/activate

* make::

    $ make dev

* Create a user account::

    $ ./manage.py createsuperuser

* If you have ssh access to the staging server, copy the database and media::

    $ fab -f scripts/fabfile.py staging get_db_dump:pycon2014
    $ fab -f scripts/fabfile.py staging get_media

  Change ``pycon2014`` in that first command to the name of your local database.

* Run local server::

    python manage.py runserver  # => http://127.0.0.1:8000/2016/ja/


Vagrantの開発環境作り
---------------------------

初めての方

* VagrandをDL&インストール http://lab.raqda.com/vagrant/
* VirtualBoxをDL&インストール https://www.virtualbox.org/

インストール後、Vagrantfileファイルのディレクトリにてターミナルより::

  vagrant up

Web開発作業手順
-----------------------------

* 課題・機能・案件ごとにJIRAにてチケットを作成、チケットごとにトピックブランチを切る(ブランチの名前はTicketID
* git-flowに乗せる。機能開発はfeatureブランチにて
* 作業完了、要レビューの際はpull request、コミッターは小松さん

スポンサー登録通知
----------------------

* 環境変数 `SLACK_SPONSOR_WEBHOOK_URL` にslackのincoming hookを登録しておくと、設定したchannelへスポンサーの登録通知が届く。


Docker support
----------------

see README-Docker.md

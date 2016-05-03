.PHONY: dev

dev:
	pip install -r pyconjp/requirements/dev.txt
	./manage.py syncdb
	./manage.py migrate
	echo "from symposion.conference import models; models.Conference.objects.create();" | ./manage.py shell
	./load_fixtures.sh

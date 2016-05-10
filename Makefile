.PHONY: dev

dev:
	pip install -r requirements/online.txt -r requirements/dev.txt
	./manage.py syncdb
	./manage.py migrate
	echo "from symposion.conference import models; models.Conference.objects.create();" | ./manage.py shell
	./scripts/load_fixtures.sh

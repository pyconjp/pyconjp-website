.PHONY: dev

dev:
	pip install -r pyconjp/requirements/dev.txt --trusted-host dist.pinaxproject.com
	echo "from symposion.conference import models; models.Conference.objects.create();" | ./manage.py shell
	./load_fixtures.sh

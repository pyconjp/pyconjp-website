#!/usr/bin/env bash

set -ex

if [ -n $DEBUG ]; then
  LC_ALL=C pip install -r requirements/dev.txt -f wheelhouse
fi

python manage.py syncdb --noinput
python manage.py migrate

python manage.py loaddata \
  fixtures/auth_user.json \
  fixtures/initial_data.json \
  fixtures/pycon.json \
  fixtures/conference.json \
  fixtures/initial_boxes.json \
  fixtures/initial_data.json \
  fixtures/proposal_base.json \
  fixtures/sitetree_menu.json \
  fixtures/sponsorship_benefits.json \
  fixtures/sponsorship_levels.json \
  fixtures/tutorials_schedule.json \
  fixtures/talks_schedule.json \
  fixtures/permissions.json \
  fixtures/teams.json \

echo "from django.contrib.auth.models import User; not(User.objects.filter(username='admin').exists()) and User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

python manage.py runserver 0.0.0.0:8000


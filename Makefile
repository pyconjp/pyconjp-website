.PHONY: dev

dev:
	pip install -r requirements/online.txt -r requirements/dev.txt
	. ./scripts/config-dev.sh
	./scripts/load_fixtures.sh

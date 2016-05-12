.PHONY: dev

dev:
	pip install -r requirements/online.txt -r requirements/dev.txt
	sh ./scripts/load_fixtures.sh


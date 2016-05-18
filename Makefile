.PHONY: dev

dev:
	pip install -f wheelhouse -r requirements/dev.txt
	sh ./scripts/load_fixtures.sh


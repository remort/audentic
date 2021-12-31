.PHONY: lint

lint:
	docker-compose run --entrypoint='sh -c "pip3 install flake8 && flake8 audentic_api/ -v --max-line-length=119  --exclude audentic_api/db/migration/versions/"' app

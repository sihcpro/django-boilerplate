IMAGE_TAG?=latest
NEW_TAG?=

run:
	PYTHONPATH=./src BE_CONF_MONGO_PASSWORD=admin123 BE_CONF_MONGO_HOST=10.1.10.224 BE_CONF_PORT=8001 python -m src.app

run-local:
	PYTHONPATH=./src python -m src.app

# Docker compose

dc-up:
	IMAGE_TAG=${IMAGE_TAG} docker-compose up 

dc-down:
	IMAGE_TAG=${IMAGE_TAG} docker-compose down

dc-update:
	IMAGE_TAG=${IMAGE_TAG} docker-compose up --detach --build

dc-build:
	IMAGE_TAG=${NEW_TAG} docker-compose build

dc-push:
	IMAGE_TAG=${IMAGE_TAG} docker-compose push 

dc-pull:
	IMAGE_TAG=${IMAGE_TAG} docker-compose pull 

dc-restart:
	make dc-pull dc-down dc-up IMAGE_TAG=${IMAGE_TAG}

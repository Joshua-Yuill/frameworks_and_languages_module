DOCKER_IMAGE:=vue_nginx_test

build:
	docker build --tag ${DOCKER_IMAGE} .
test:
	docker run --rm --publish 8001:8001 ${DOCKER_IMAGE}

ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

serve-dev:
	@docker run -it --rm --publish="4000:4000" --volume=${ROOT_DIR}:/srv/jekyll jekyll-dev

build-dev-docker-image:
	@docker build . -f Dev.Dockerfile  --tag='jekyll-dev'

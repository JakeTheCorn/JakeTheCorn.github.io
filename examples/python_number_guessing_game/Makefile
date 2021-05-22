ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

run-shell:
	@docker run \
    -it \
    --volume="${ROOT_DIR}":/python_number_guessing_game \
    --rm \
    --workdir=/python_number_guessing_game \
    python:3.10.0b1-alpine3.13 \
        /bin/sh;

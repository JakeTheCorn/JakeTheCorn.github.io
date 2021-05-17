FROM python:3.10.0b1-slim-buster
RUN apt-get update
RUN apt-get -y install watch
RUN mkdir /app
WORKDIR /app
CMD watch python3 -m unittest discover --pattern='*_tests.py'

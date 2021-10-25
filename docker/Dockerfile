FROM python:3.9.6-alpine3.14

ENV PYTHONUNBUFFERED 1

ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

RUN mkdir /code

WORKDIR /code

RUN pip3 install --upgrade pip

ADD requirements.txt requirements.txt 

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    gcc musl-dev python3-dev libpq libffi-dev openssl-dev cargo && \
    pip3 install -r ./requirements.txt && \
    apk del .build-deps

ADD . /code

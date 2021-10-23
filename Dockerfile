FROM python:3-alpine

# deps
RUN apk add --update git; \
    apk add --update bash; \
    apk add --update openssl-dev; \
    apk add --update libffi-dev; \
    apk add --update build-base; \
    pip install --upgrade pip;

WORKDIR /code
ADD . /code

RUN pip install -r requirements.txt
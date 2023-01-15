# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apk update && apk add curl && apk add git && rm -rf /var/cache/apk/*
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev openssl-dev
RUN pip install -r requirements.txt
COPY . .

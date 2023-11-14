FROM python:3.9-alpine3.16

WORKDIR /social_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /social_api
COPY ./requirements.txt /social_api/requirements.txt
EXPOSE 8000

RUN pip install --upgrade pip

RUN apk add postgresql-client && apk add build-base && apk add postgresql-dev && rm -f /var/lib/apt/lists/*

RUN pip install -r requirements.txt
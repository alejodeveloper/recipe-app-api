FROM python:3.9-alpine
MAINTAINER Alejo Dev

# TELLS PYTHON RUN UNBUFFERED MODE
ENV PYTHONUBUFFERED 1

COPY ./requirements.txt /requirements.txt
# INSTALL POSTGRESQL CLIENT
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .temp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# CREATE USER FOR RUN APPLICATIONS ONLY
RUN adduser -D user
USER user

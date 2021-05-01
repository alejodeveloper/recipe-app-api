FROM python:3.9-alpine
MAINTAINER Alejo Dev

# TELLS PYTHON RUN UNBUFFERED MODE
ENV PYTHONUBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# CREATE USER FOR RUN APPLICATIONS ONLY
RUN adduser -D user
USER user




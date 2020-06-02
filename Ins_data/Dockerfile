FROM python:latest

RUN apt-get update \
    && apt-get upgrade -y

RUN apt-get install -y vim
RUN pip install --upgrade pip
RUN pip install neo4j graphene

WORKDIR /usr/src/app


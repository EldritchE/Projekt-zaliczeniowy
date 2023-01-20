# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR app
COPY requirements.txt requirements.txt
COPY password_manager password_manager
COPY przykladowe_db przykladowe_db
COPY run.sh run.sh
COPY run-dev.sh run-dev.sh
RUN mkdir -p db
RUN pip3 install -r requirements.txt

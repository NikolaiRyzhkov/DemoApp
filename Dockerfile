FROM python:3.12-alpine3.19

COPY requirements.txt /temp/requirements.txt
COPY demoAppProject /demoAppProject
WORKDIR demoAppProject
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password main-user

USER main-user

FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./core /app



# Dockerfile

FROM python:3.13.5-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get install -y gcc libpq-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
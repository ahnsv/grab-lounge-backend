FROM python:3.8.7-slim-buster

COPY src /app/src
COPY requirements.txt /app/requirements.txt
WORKDIR /app
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

RUN pip install pip==21.2.4 && \
    pip install -r requirements.txt

# Feel free to change base image
FROM python:3.8-slim-buster

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

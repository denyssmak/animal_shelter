FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /animal_shelter

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt ./requirements.txt
# COPY init.sql /docker-entrypoint-initdb.d/  # not working

RUN pip install -r requirements.txt

COPY . .



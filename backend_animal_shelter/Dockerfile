FROM python:3.9-alpine

WORKDIR /animal_shelter

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt ./requirements.txt
# COPY init.sql /docker-entrypoint-initdb.d/  # not working

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]

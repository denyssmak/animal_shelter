FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /animal_shelter

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt ./requirements.txt
# COPY init.sql /docker-entrypoint-initdb.d/  # not working

RUN pip install -r requirements.txt
RUN apt-get update && \
    apt-get install -y xfonts-75dpi xfonts-base && \
    wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb && \
    dpkg -i wkhtmltox_0.12.6-1.buster_amd64.deb
COPY . .
ENTRYPOINT ["sh"]


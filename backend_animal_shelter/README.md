## Setup Project

    docker-compose build
    docker-compose up

### Setup db in the postgres container
    enter the postgres container:
    docker ps
    docker exec -ti {CONTAINER ID} bash
    psql -U postgres
    CREATE DATABASE animal_shelter;
    GRANT ALL ON DATABASE animal_shelter TO postgres;

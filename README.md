# Metamemo

## Installation with docker

Clone the repository, copy `.env-example` to `.env` and edit accordingly. Then run `docker compose up -d` to have the whole app up in seconds.

Once docker compose is done, you should run these commands ONCE:

```shell
docker compose run metamemo poetry run python src/manage.py migrate
docker compose run metamemo poetry run python src/manage.py createsuperuser
```

## Installation without docker

Clone the repository, copy `.env-example` to `.env` and edit accordingly. Make sure you have python 3.8 and poetry installed. Then run `poetry install`. Finally, once you have all the required services running (mariadb, redis, minio), run the following commands:

```shell
poetry run python src/manage.py migrate
poetry run python src/manage.py createsuperuser
poetry run python src/manage.py runserver
```

### ATTENTION!

We strongly recommend using MariaDB as it was the database metamemo was developed on. Use the following command to create the database from the database shell:

```sql
CREATE DATABASE metamemo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

If you're running metamemo via docker compose, we already ensure this, don't worry.

You should be able to visit your metamemo instance at http://localhost:8000/admin/

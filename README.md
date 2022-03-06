# Metamemo

## Installation

Clone the repository, copy `.env-example` to `.env` and edit accordingly. Make sure you have poetry installed and run `poetry install`. Finally, run the following commands:

```shell
poetry run python src/manage.py migrate
poetry run python src/manage.py runserver
```

### ATTENTION!

We strongly recommend using MariaDB as it was the database metamemo was developed on. Use the following command to create the database from the database shell:

```sql
CREATE DATABASE metamemo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

You should be able to visit your metamemo instance at http://localhost:8000/admin/

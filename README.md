## Installation and Configuration Guide

### Prerequisites

- Python 3.x installed
- Poetry

> Note: [Poetry Installation](https://python-poetry.org/docs/#installation)

### Step 1: Clone the Project Repository

```bash
git clone https://github.com/ericopieri/django_texo.git
```

### Step 2: Package Installation and Virtual Environment Creation

Commands designated for installing required project packages, creating and activating the virtual environment to run the project.

```
cd django_texo
poetry config virtualenvs.in-project true
poetry install
poetry shell
```

> **Note:** It's important that all commands run internally in Django from here onwards are executed with the virtual environment activated (`poetry shell`).

## Step 3: Migrating Databases

Run both migrations sequentially, which will create database files (default and test).

```
poetry run python manage.py migrate
poetry run python manage.py migrate --database=test
```

## Step 4: Dumping Data from CSV for Application Functionality

The `dump_movie_data` command will parse the required movie CSV and add items to the database.

```
poetry run python manage.py dump_movie_data
```

## Step 5: Running the Application! Voilà!

Run the command to start the application. [Access here!](http://localhost:8000/)

```
poetry run python manage.py runserver
```

## Step 6: Running Integration Tests

Test data has been mocked.

```
poetry run python manage.py test
```

## Step 7: Accessing the Proposal Endpoint

**/api/maxminwinnerinterval/** - This endpoint returns, in a JSON data set, the producer with the longest interval between two consecutive awards, and the one who
obtained two awards the fastest.

Endpoint proposed by the challenge.

## Below is a guide on how to use the other endpoints contained in the application

**/api/movies/** - List of all movies and creation of new movies (GET and POST)
**/api/movies/\<pk\>/** - Details of a specific movie, updating or removing it (replace <pk> with the movie ID) (GET, PUT, and DELETE)

**Structure for adding or updating movies:**<br>

```
{
    "title": "Movie",
    "year": 0000,
    "winner": false,
    "studios": ["Studio Name 1", "Studio Name 2"],
    "producers": ["Producer Name 1", "Producer Name 2]
}
```

/api/producers/ - List of all producers and creation of new producers (GET and POST)
/api/producers/<pk>/ - Details of a specific producer, updating or removing it (replace <pk> with the producer ID) (GET, PUT, and DELETE)

**Structure for adding or updating producers:**<br>

```
{
    "name": "Producer Name"
}
```

/api/studios/ - List of all studios and creation of new studios
/api/studios/<pk>/ - Details of a specific studio, updating or removing it (replace <pk> with the studio ID) (GET, PUT, and DELETE)

**Structure for adding or updating studios:**<br>

```
{
    "name": "Studio Name"
}
```

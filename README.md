# Youtube data project

The REST application allows you to receive information on requests from YouTube. For example, you can get the most relevant videos for a search term. You can also set filtering.
The application allows you to update data on current requests using the Celery task.

## Build project and start coding

First of all, you must clone the repository and activate the virtual environment.

After, install the required dependencies:

```bash
$ pip install -r requirements.txt
```

Make a migrations:

```bash
$ python manage.py migrate
```

Run web server locally:

```bash
$ python manage.py runserver
```

Happy Coding!


## Environment variables


Some of the project settings are taken from environment variables.

There are variables available:

SECRET_KEY - project secret key. Required for local and production.

DEBUG - Set 'False' to production.

DATABASE_URL - Url to use database. For example: postgres://user:password@0.0.0.0:5432/database

YOUTUBE_API_KEY - Youtube api key

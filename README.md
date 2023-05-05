# todo-microservice-flask

A simple microservice with Python and Flask

#### Setup

* Execute `virtualenv venv -- p ython=python3.11`
* Execute `source venv/bin/activate` (or `deactivate`)

#### Installation

* Execute `pip install flask`
* Execute `pip freeze` to loack down dependencies.
* Other option is if you already have a `requirements.txt` just execute `pip install -r requirements.txt` to install all teh required pendendencies.

#### Execution

* Execute `./run.sh` or 	`flask run`, notices if you haven setup `FLASK_APP` and `FLASK_ENV` execute `export FLASK_APP=main.py` or set up the `.flaskenv` file and run `pip install python-dotenv`

#### Resources

* [Demonstrates how to use Python, Flask, and Docker to quickly prototype and build microservices](https://github.com/cloudacademy/python-flask-microservices)
* [Editing Python Code in Visual Studio Code](https://code.visualstudio.com/docs/python/editing)

#### API Resources

* [Flask REST API Tutorial - Python Tutorial (pythonbasics.org)](https://pythonbasics.org/flask-rest-api/)
* [How to Build a REST API With Flask and Postgres Database (makeuseof.com)](https://www.makeuseof.com/build-rest-api-with-flask-and-postgres/)

#### Database Resources

* [Understanding connection URI strings in PostgreSQL (prisma.io)](https://www.prisma.io/dataguide/postgresql/short-guides/connection-uris)
* [Python Error Handling with the Psycopg2 PostgreSQL Adapter 645 | ObjectRocket](https://kb.objectrocket.com/postgresql/python-error-handling-with-the-psycopg2-postgresql-adapter-645)

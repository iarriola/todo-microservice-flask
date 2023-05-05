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
* [Python Application Layouts: A Reference – Real Python](https://realpython.com/python-application-layouts/)
* [Development Mode (a.k.a. “Editable Installs”) - setuptools 67.7.2.post20230503 documentation (pypa.io)](https://setuptools.pypa.io/en/latest/userguide/development_mode.html)
* [src layout vs flat layout — Python Packaging User Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
* [joshuavaple/melhousing: Melbourne housing market data analysis, packaging style (github.com)](https://github.com/joshuavaple/melhousing/tree/main)
* [Guide to Python Project Structure and Packaging | by Joshua Phuong Le | MLearning.ai | Medium](https://medium.com/mlearning-ai/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95)
* [The Good way to structure a Python Project | by Najma Bader | Towards Data Science](https://towardsdatascience.com/the-good-way-to-structure-a-python-project-d914f27dfcc9)
* [Structuring Your Project — The Hitchhiker&#39;s Guide to Python (python-guide.org)](https://docs.python-guide.org/writing/structure/)

#### API Resources

* [Flask REST API Tutorial - Python Tutorial (pythonbasics.org)](https://pythonbasics.org/flask-rest-api/)

#### Database Resources

* [Understanding connection URI strings in PostgreSQL (prisma.io)](https://www.prisma.io/dataguide/postgresql/short-guides/connection-uris)
* [Python Error Handling with the Psycopg2 PostgreSQL Adapter 645 | ObjectRocket](https://kb.objectrocket.com/postgresql/python-error-handling-with-the-psycopg2-postgresql-adapter-645)
* [How to Build a REST API With Flask and Postgres Database (makeuseof.com)](https://www.makeuseof.com/build-rest-api-with-flask-and-postgres/)

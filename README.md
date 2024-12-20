## Built with

The project was developed from scratch with Frontend and Backend technologies, for the communication between the client and the server I implemented a REST API, which is responsible for returning the necessary data in JSON format to the client:

- Frontend:
  - Angular
  - SCSS
  - PrimeNG Components

- Backend:
  - Python (Flask)
  - SQLite (As database manager)
  - Flask Migrate (To perform migrations)
  - SQLAlchemy and Flask SQLAlchemy (Python SQL toolkit and ORM that gives application developers the full power and flexibility of SQL)
  - REST API (For communication between client and server)

## Project requirements and how to use it

For the project you must run both development environments at the same time, both the Frontend and the Backend. In the Frontend you will find JavaScript technologies (Angualr) and in the Backend you will find Python technologies and tools (Flask), so you must have NodeJS and Python installed on your computer (As a reference this project was developed with version 3.9.6 of Python and 18.12.1 of NodeJS).

I leave you links to NodeJS and Python for installation:
  - [NodeJS website](https://nodejs.org/en/)
  - [Python website](https://www.python.org/)

First of all download the project to start using it, do it from the terminal:

```shell
$ git clone https://github.com/Skizaru/todo_app.git

$ cd todo_app
```

If you did it correctly and there were no problems, you should see these folders in your terminal:

```shell
/backend
/frontend
README.md

### Frontend

If you already have NodeJS installed on your computer perform the following steps to run the Frontend (Remember that the Backend must be running):

1. Move to the `/frontend` folder and run the following command to install the necessary:

```shell
# This will install what you need for the Frontend (npm comes with NodeJS after installation)
$ npm install
```

2. Then you will need to run the following command to start running the Frontend:

```shell
$ npm start
```

3. That's all for the Frontend, if you haven't run the Backend yet, continue with the next section (Backend)

### Backend

If you already have Python installed on your computer perform the following steps to run the Backend

1. Move to the `/backend` folder and run the following command to create a virtual development environment with Python:

```shell
# If it doesn't work this way try "python3", this will depend on how you installed Python on your computer
$ python -m venv venv
```

2. Now activate the development environment and install the necessary requirements found in the `requirements.txt` file:

```shell
# This is how it is done in Linux, in Windows it is as follows "venv\Scripts\activate"
$ . venv/bin/activate
# Now install the necessary requirements using "pip" or "pip3",
# this will depend on how you installed Python on your computer
(venv) $ pip install -r requirements.txt

### REST API

Everything related to the API is inside `flaskr/`. The following table summarizes the routes that were implemented:

| HTTP Method | Resource URL           | Notes                                   |
| ----------- | -------------------    | --------------------------------------- |
| `GET`       | */api/v1/tasks*        | Return the collection of all tasks.     |
| `GET`       | */api/v1/tasks/id*     | Return a single task.                   |
| `POST`      | */api/v1/tasks*        | Register a new task.                    |
| `PUT`       | */api/v1/tasks/id*     | Modify the values of a task.            |
| `DELETE`    | */api/v1/tasks/id*     | Delete a task from the collection.      |
# TodoApp

This project is a Todo application consisting of an Angular frontend and a Flask backend. The project uses Docker and Docker Compose to facilitate deployment and execution.

## Project Structure

The project is structured as follows:

- **backend/**: Contains the backend source code in Flask.
- **frontend/**: Contains the frontend source code in Angular.
- **docker-compose.yml**: Configuration file for Docker Compose.
- **models/**: Contains TensorFlow models for the prediction service.

## Dockerfile

The project uses two Dockerfiles:

- One for the backend, located in `Dockerfile`.
  The Dockerfile for the backend uses a Python image, copies the source code, installs the dependencies, and exposes port 5000 to run the Flask application.

- One for the frontend, located in `Dockerfile`.
  The Dockerfile for the frontend uses a Node.js image to build the Angular application, then an Nginx image to serve the built application, exposing port 80.

## Docker Compose

The `docker-compose.yml` file defines the services for the backend, frontend, MySQL, phpMyAdmin, and the TensorFlow service. It allows you to start all the necessary services with a single command.

## Installation and Launch

To install and launch the project with a single command, make sure you have Docker and Docker Compose installed on your machine. Then, run the following command at the root of the project:

```sh
docker-compose up --build
```

This command will build the Docker images for the backend and frontend, then start all the services defined in the `docker-compose.yml` file.

## Access to Services

- **Frontend**: [http://localhost](http://localhost)
- **Backend**: [http://localhost:5000](http://localhost:5000)
- **phpMyAdmin**: [http://localhost:8080](http://localhost:8080)
- **TensorFlow Serving**: [http://localhost:8501](http://localhost:8501)

## Database Seeding

To insert initial data into the database, run the `seed.py` script in the backend container.

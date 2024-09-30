![alt text](logo-teal.png "FastAPI")

# FASTAPI BASE

## Introduction

With the aim of building a FastAPI Base project framework that is ready for use in an enterprise environment,
and at the same time helping those who are interested in learning the FastAPI framework understand how to implement theoretical knowledge into a real-world project.

The project also provides the most basic features: CRUD User, Login, Register.

Finally, we welcome any feedback to make the project more complete.

## Technology Stack and Features

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
  - 🧰 [SQLModel](https://sqlmodel.tiangolo.com) for the Python SQL database interactions (ORM).
  - 🔍 [Pydantic](https://docs.pydantic.dev), used by FastAPI, for the data validation and settings management.
  - 💾 [PostgreSQL](https://www.postgresql.org) as the SQL database.
- 🔒 Secure password hashing by default.
- 🔑 JWT (JSON Web Token) authentication.
- 🛡️ Authorization.
- 🌍 Configure environment variables using pydantic-settings
- ⚙️ Configure logging through the logging.ini file
- 🛠️ Pre-implement some sample middlewares and dependencies
- ⚠️ Exception handle

## Installation

**Method 1:**

- Clone Project
- Install Postgresql & Create Database & Create table Users
- Install requirements.txt
- Run the project on port 8000

```
// Create table Users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user'
);

// Clone project & run
$ git clone https://github.com/sy-duc/training-fastapi
$ cd training-fastapi
$ python -m venv venv
$ .\venv\Scripts\activate
$ pip install -r requirements.txt
$ cp env.example .env       // Recheck SQL_DATABASE_URL
$ cd app
$ python main.py
```

**Method 2:** Using Docker & Docker Compose

## Project Structure

```
.
├── alembic              // If using Alembic to manage database migrations, there will be a folder to contain the migration files.
├── app
│   ├── api              // Contains API endpoints organized by version (v1/, v2/...), making it easy to extend API versions in the future.
│   ├── core             // Contains a config file to load environment variables, database connectivity, and functions to create/verify JWT access tokens.
│   ├── crud             // Contains CRUD (Create, Read, Update, Delete) operations for each model.
│   ├── helpers          // Includes supporting functions such as exception handling, pagination, etc.
│   ├── middlewares      // Middleware for setting up CORS and logging.
│   ├── models           // Database model
│   ├── schemas          // Pydantic Schema
│   ├── services         // Contains CRUD logic for interacting with the database.
│   ├── dependencies.py  // The dependencies for authentication and authorization.
│   └── main.py          // Main configuration for the entire project.
├── .gitignore
├── alembic.ini
├── Dockerfile
├── env.example          // Sample for the .env file.
├── logging.ini          // Logging configuration.
├── README.md
└── requirements.txt     // File containing libraries to be installed via pip.
```

## To be added in the future

- 🧪 Pagination.
- 📫 Email based password recovery (or OTP authentication).
- ✅ Tests with [Pytest](https://pytest.org).
- 🐋 [Docker Compose](https://www.docker.com) for development and production.

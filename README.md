# `cyber-students`

This repository provides some sample code for the Shared Project for
Modern Cryptography and Security Management & Compliance.  The project
requires Python 3 and MongoDB.

## Setup the Project

Create a Python 3 virtual environment:

```sh
python3 -m venv project-venv
source project-venv/bin/activate
```

Install the required packages:

```sh
cd cyber-students
pip3 install -r requirements.txt
```

Install and start MongoDB.

Create the MongoDB databases:

```
mongo

use cyberStudents;
db.createCollection('users');

use cyberStudentsTest;
db.createCollection('users');
```

## Test the Project

You can run the automated tests using:

```sh
python3 run_test.py
```

## Start the Project

To start the server:

```sh
python3 run_server.py
```

The server is available on port 4000 at http://localhost:4000/students/api.

## Usage

To register a new user:

```sh
curl -X POST http://localhost:4000/students/api/registration -d '{"email": "foo@bar.com", "password": "pass", "displayName": "Foo Bar"}'
```

## Tokens

A token expires and is intended to be short-lived. A token expires two
hours after login, after a logout, or if there is another login from
the same user, generating a new token.

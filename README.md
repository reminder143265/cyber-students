# `cyber-student-survey`

This repository provides some sample code for the Shared Project for
Modern Cryptography and Security Management & Compliance.  The project
requires Python 3 and MongoDB.

## Setup

Install Python 3 and the required libraries.

```sh
pip3 install -r requirements.txt
```

Install and start MongoDB.

To start the server:

```sh
python3 run_server.py
```

The server is available on port 4000.

## Test the Project

You can run the automated tests using:

```sh
python run_test.py
```

## Usage

To check that the server is running:

```sh

http://localhost:4000/cyber/api

To register a new user:

```sh
curl -X POST http://localhost:4000/cyber/api/registration -d '{"email": "foo@bar.com", "password": "pass", "displayName": "Mr. Foo Bar"}'
```

## Tokens

A token expires and is intended to be short-lived. A token expires two
hours after login, after a logout, or if there is another login from
the same user, generating a new token.

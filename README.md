# MU22 Frontend Assignment 1

## About

A recipe helper that lets you adjust amounts and review recipes.

Comes with a simple backend.

## Setup

Create a virtual environment in the repository root:

    python -m venv .venv

Activate virtual environment:

Windows

    .\.venv\scripts\activate

Posix

    ./.venv/bin/activate

Install dependencies into our virtual environment:

    python -m pip install -r requirements.txt

## Run

To run, execute the following:

    python local.py

This will run te server using uvicorn on port 8080.

## Usage

| Page | URL |
| --- | --- |
| Recipe page | http://lohalhost:8080 |
| Swagger | http://localhost:8080/api-doc |

## REST Api

See Swagger page (Usage).

| Path | Description |
| --- | --- |
| GET /recipes | Get recipes. |
| POST /recipes | Import recipes into database. |
| POST /review | Post a review for a recipe. |

## Notes

The database file is included in this git repo. It is safe to delete, because the app will recreate
an empty one. The json for the recipes is in the root folder and can be used to
import to the empty database (POST to /recipes).

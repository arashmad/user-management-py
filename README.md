# FastAPI Poetry Boilerplate

A boilerplate project for fastapi python project supported by poetry.

## Resources

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![codecov](https://codecov.io/gh/arashmad/user-management-py/graph/badge.svg?token=Qe6LGpP4oh)](https://codecov.io/gh/arashmad/user-management-py)

Poetry helps you declare, manage and install dependencies of Python projects,
ensuring you have the right stack everywhere.

## Installation

```bash
# Install Poetry
pipx install poetry
# Download the source code
git clone https://github.com/arashmad/user-management-py.git
# Install dependencies
cd fastAPI-poetry-boilerplate
poetry install
# Activate virtual environment
poetry shell
# Test the code and installation
make lint && make test
```

## Custom Usage

You can also use the project as a template for your own project. To do that you can use [this bash file](https://gist.github.com/arashmad/fb1f58c88710594df3ecdc5b3387f03b).

```bash
git clone https://gist.github.com/fb1f58c88710594df3ecdc5b3387f03b.git
chmod +x fastapi_boilerplate_builder.sh
```

Once you run it, you will be prompted for the following questions:

- Directory of the cloned repository
- Directory of the generated instance
- Slug name

It generates an instance of the project for you and test it to make sure it is working.

After create a new repository on github (with the same slug name an without readme file) follow commands in your terminal to push your intance to github.

To make sure your instance is working you can see the action tabs on github page.

## Developed and Maintained By

**Arash Madadi**

Full Stack Developer & Geospatial Expert

Deutsches GeoForschungsZentrum GFZ

Sektion 1.4 (Fernerkundung und Geoinformatik)

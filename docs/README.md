# Virus! Documentation

Do you want to live the experience of playing `Virus!`
from your pc and/or mobile, without spending money to
buy the cards? This app makes that dream come true!

It includes also `Virus! 2 Evolution` and `Virus! Halloween` expansions.

## Prerequisites

We use [Poetry](https://python-poetry.org/docs/).
Please follow the installation guide.

## Commands

### Installation

```shell
poetry shell

poetry install

pre-commit install
```

### Test

```shell
pytest

mypy --strict virus tests

pre-commit run --all-files
```

### Update

```shell
pipx upgrade poetry

poetry update

pre-commit autoupdate
```

### Poetry commands cheatsheet

- `poetry shell`: activates the virtual environment
- `poetry install`: installs the project, along with its dependencies.
  - If `poetry.lock` does not exist, it will create it.
  - If `poetry.lock` exists, it uses the dependencies exact versions listed in it
- `poetry install --no-root`: installs only dependencies
- `poetry add X`: adds a dependency
- `poetry run python x.py`: Runs a python script
- `poetry run X`: runs a command line tool, like pytest or black

More commands can be found [here](https://python-poetry.org/docs/cli/).

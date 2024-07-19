# FPL Prediction System

This project aims to develop a high-performance machine learning model capable of predicting the expected points of FPL players.

## Setup

1. Install Poetry: `curl -sSL htpps://install.python-poetry.org | python3 -`
2. Install dependencies: `poetry install`
3. Initialize the database: `python src/data_collection/models.py`
4. Run data collection: `python src/data_collection/fpl_api.py`

## Development

This project uses pre-commit hooks to maintain code quality. After cloning the repository, run:

```bash
pre-commit install
```

This will set up the pre-commit hooks for your local repository.

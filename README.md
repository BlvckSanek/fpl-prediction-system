# FPL Prediction System

**Objective: To develop a high-performance machine learning model capable of predicting the expected points of Fantasy Premier League (FPL) players, with real-time updates and integration into Google Sheets.**

## Project Overview

This project aims to:

1. Collect and process FPL data
2. Develop and train a machine learning model for point predictions
3. Create a real-time API for predictions
4. Integrate the prediction system with Google Sheets for easy user access

## Setup

1. Install Poetry: `curl -sSL https://install.python-poetry.org | python3 -`
2. Install dependencies: `poetry install`
3. Initialize the database: `python src/data_collection/models.py`
4. Run data collection: `python src/data_collection/fpl_api.py`

## Development

This project uses pre-commit hooks to maintain code quality. After cloning the repository, run:

```bash
pre-commit install
```

This will set up the pre-commit hooks for your local repository.

## Project Structure

```markdown
fpl_prediction_system/
│
├── data/
│   ├── raw/                  # Raw data collected from FPL API
│   └── processed/            # Processed and feature-engineered data
├── src/
│   ├── data_collection/      # Scripts for collecting data from FPL API
│   ├── data_processing/      # Data cleaning and feature engineering
│   ├── model/                # Machine learning model development
│   ├── api/                  # FastAPI application for serving predictions
│   └── sheets_integration/   # Google Sheets integration scripts
├── models/                   # Saved model files
├── tests/                    # Unit and integration tests
├── docs/                     # Project documentation
├── config/                   # Configuration files
├── scripts/                  # Utility scripts
├── .github/
│   └── workflows/            # GitHub Actions CI/CD workflows
├── infrastructure/
│   └── terraform/            # Terraform configurations for deployment
├── .pre-commit-config.yaml   # Pre-commit hook configurations
├── pyproject.toml            # Poetry dependency management
├── .gitignore
└── README.md
```

## Contributing

As this is a collaborative project, we welcome contributions from all team members. Here are some guidelines to follow:

1. **Branching**: Create a new branch for each feature or bug fix you're working on.

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Commits**: Make small, logical commits with clear messages describing the changes.

   ```bash
   git commit -m "Add data validation for player statistics"
   ```

3. **Pull Requests**: When your feature is complete, create a pull request for review.

4. **Code Style**: Follow PEP 8 guidelines for Python code. Our pre-commit hooks will help enforce this.

5. **Testing**: Add appropriate unit tests for new functionality.

6. **Documentation**: Update relevant documentation, including this README, when making significant changes.

7. **Communication**: Use GitHub Issues for task tracking and discussions about features or bugs.

## License

This project is licensed under the MIT License. This means you're free to modify, distribute, and use the code in your own projects, including commercial ones, as long as you include the original copyright and license notice.

For the full license text, please see the [LICENSE](LICENSE) file in the repository.

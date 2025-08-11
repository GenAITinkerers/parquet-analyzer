# Parquet-Analyzer
- Data Processing & Analysis Project

This project provides a modular framework for processing data (CSV to Parquet), performing analytical computations, and preparing it for machine learning training. It is containerized using Docker and includes unit tests for production readiness.

Includes utilities, Jupyter notebooks, and Docker support for reproducible data science workflows.

## Features

- Load and validate Parquet and CSV data
- Compute statistics (mean, median, etc.) via modular services
- Jupyter notebooks for interactive exploration
- Docker and Docker Compose for easy deployment
- Unit tests with pytest and coverage
- Convert raw CSV data to optimized Parquet format
- Modular data transformation services (mean, median, etc.)
- Configurable and reusable data loading logic
- Unit tests with pytest
- Docker and Docker Compose support
- Jupyter notebooks for EDA and development


## Project Structure
This project is organized as follows:

- `src/` – Main source code including core logic and utilities.
- `tests/` – Unit tests for source code.
- `data/` – Folder to hold raw, processed, and external data files.
- `notebooks/` – Jupyter notebooks for experimentation and prototyping.
- `Dockerfile`, `docker-compose.yml` – Container setup for deployment and development.


```
├── Dockerfile
├── docker-compose.yml
├── setup.py
├── setup.cfg
├── data/
│   ├── raw/
│   │   └── training_data.csv
│   ├── processed/
│   └── external/
├── notebooks/
│   ├── calculator.ipynb
│   ├── csv_to_parquet.ipynb
│   ├── load_data.ipynb
│   └── load_parquet_data.ipynb
├── src/
│   └── parquet/
│       ├── __init__.py
│       ├── calculator.py
│       ├── service1_mean.py
│       ├── service2_median.py
│       └── ... (other modules)
├── tests/
│   ├── test_calculator.py
│   ├── test_load_parquet1.py
│   └── ... (other tests)
└── README.md
```

## Project setup
- choose appropriate python enviornment
## Installation

From the project root (where `setup.py` is located):

```sh
pip install -U setuptools setuptools_scm wheel
```
```sh
python setup.py bdist_wheel
```
```sh
pip install dist/*.whl
```


## How to Run:
- copy testenv from test folder. Rename it as `.env`.
- If you wish to use config.py from your local project, add this `.env` two level up config.py so that according to definition in config.py, the config parameters are read from this location.
- If you wish to use config.py from project installed as package, add this `.env` two level up config.py in installed package location so that accroding to definion in config.py and call to this config.py, the config paramets are read from this location in package


# Unit Test
Run all unit tests with coverage:
```sh
pytest
```
or with converage reporting:
```sh
pytest --cov=parquet --cov-report=term-missing
```

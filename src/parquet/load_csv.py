"""
Load training data for machine learning model.
This read data from from a file in specified folder path and returns it as a pandas DataFrame
"""

import pandas as pd
import os
import logging
from pathlib import Path

from parquet.util import setup_logger

LOGGER = setup_logger(__name__, logging.INFO)

def load_csv_data(folder_path: str, file_name: str) -> pd.DataFrame:
    """
    Load aggregated data from a CSV file and return it as a DataFrame.

    Args:
        folder_path (Path | str): Path to the folder containing the file.
        file_name (str): Name of the CSV file containing aggregated data.

    Returns:
        pd.DataFrame: DataFrame containing the training data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty, contains null values, or has invalid data.
        PermissionError: If the file is not readable.
    """
    folder_path = Path(folder_path)
    file_path = folder_path / file_name
    LOGGER.info(f"Loading data from {file_path}")

    # Perform all validation checks before loading the data
    if not file_path.exists():
        LOGGER.error(f"The file {file_path} does not exist.")
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    if file_path.suffix != ".csv":
        LOGGER.error(f"The file {file_path} is not a CSV file.")
        raise ValueError(f"The file {file_path} is not a CSV file.")

    if not os.access(file_path, os.R_OK):
        LOGGER.error(f"The file {file_path} is not readable.")
        raise PermissionError(f"The file {file_path} is not readable.")

    LOGGER.info(f"File {file_path} exists and is readable. Proceeding with loading data.")
    df = pd.read_csv(file_path)

    if df.empty:
        LOGGER.warning("The DataFrame is empty after loading data.")
        raise ValueError(f"The file {file_path} contains no data.")

    if df.isnull().values.any():
        LOGGER.warning("The DataFrame contains null values.")
        raise ValueError(f"The file {file_path} contains null values.")

    LOGGER.info(f"Data loaded for training from {file_path} with shape {df.shape}")
    return df



if __name__ == "__main__":
    # Example usage
    folder_path = "data/raw"
    file_name = "training_data.csv"
    try:
        df = load_csv_data(folder_path, file_name)
        print(f"Data loaded successfully with shape {df.shape}")
    except Exception as e:
        LOGGER.error(f"Error loading data: {e}")


    print("application break or not stop")
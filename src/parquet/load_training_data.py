"""
Load training data for machine learning model.
This read data from from a file in specified folder path and returns it as a pandas DataFrame.
"""

# in build
import logging
import pandas as pd
from pathlib import Path
import os

# user defined
from parquet.util import setup_logger



setup_logger()
LOGGER = logging.getLogger(__name__)

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

def load_parquet_data(folder_path: str, file_name: str) -> pd.DataFrame:
    """
    Load aggregated data from a Parquet file and return it as a DataFrame.

    Args:
        folder_path (Path | str): Path to the folder containing the file.
        file_name (str): Name of the Parquet file containing aggregated data.

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
    # check if the file exists
    if not file_path.exists():
        LOGGER.error(f"The file {file_path} does not exist.")
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # check if the file is a valid parquet file
    if file_path.suffix != ".parquet":
        LOGGER.error(f"The file {file_path} is not a Parquet file.")
        raise ValueError(f"The file {file_path} is not a Parquet file.")
    
    # check if the file is readable
    if not os.access(file_path, os.R_OK):
        LOGGER.error(f"The file {file_path} is not readable.")
        raise PermissionError(f"The file {file_path} is not readable.")
    
    LOGGER.info(f"File {file_path} exists and is readable. Proceeding with loading data.")
    df = pd.read_parquet(file_path)

    # Validate the DataFrame after loading
    # Check if the DataFrame is empty
    if df.empty:
        LOGGER.warning("The DataFrame is empty after loading data.")
        raise ValueError(f"The file {file_path} contains no data.")
    
    # Check for null values
    if df.isnull().values.any():
        LOGGER.warning("The DataFrame contains null values.")
        raise ValueError(f"The file {file_path} contains null values.")
    
    LOGGER.info(f"Data loaded for training from {file_path} with shape {df.shape}")
    return df

if __name__ == "__main__":
    # Example usage for CSV
    print(f"Current working directory: {Path.cwd()}")
    folder_path = "artifacts/input"
    file_name = "training_data.csv"
    print(f"Using data path: {folder_path}")
    try:
        data = load_csv_data(folder_path, file_name)
        print(data.head())
    except Exception as e:
        LOGGER.error(f"Failed to load training data: {e}")

    # Example usage for Parquet
    parquet_file_name = "training_data.parquet"
    try:
        parquet_data = load_parquet_data(folder_path, parquet_file_name)
        print(parquet_data.head())
    except Exception as e:
        LOGGER.error(f"Failed to load Parquet training data: {e}")
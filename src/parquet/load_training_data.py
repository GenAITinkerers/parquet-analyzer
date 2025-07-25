"""
Load training data for machine learning model.
This read data from from a file in specified folder path and returns it as a pandas DataFrame.
"""

# in build
import logging
import pandas as pd
from pathlib import Path

# user defined
from parquet.util import setup_logger



setup_logger()
LOGGER = logging.getLogger(__name__)

def load_csv_data(folder_path: Path | str, file_name: str) -> pd.DataFrame:
    """
    Load Aggregated data from a CSV file and return it as a DataFrame.

    Args:
        folder_path (Path | str): Path to the folder containing aggregated data.
        file_name (str): Name of the CSV file containing aggregated data.

    Returns:
        pd.DataFrame: DataFrame containing the training data.
    """
    folder_path = Path(folder_path)
    file_path = folder_path / file_name
    print(f"Loading data from: {file_path}")
    LOGGER.info(f"Loading data from {file_path}")
    try:
        df = pd.read_csv(file_path, parse_dates=True)
        LOGGER.info(f"Data loaded successfully with shape {df.shape}")
        return df
    except Exception as e:
        LOGGER.error(f"Error loading  data: {e}")
        raise

def load_parquet_data(folder_path: Path | str, file_name: str) -> pd.DataFrame:
    """
    Load data from a Parquet file and return it as a DataFrame.

    Args:
        folder_path (Path | str): Path to the folder containing the Parquet file.
        file_name (str): Name of the Parquet file.

    Returns:
        pd.DataFrame: DataFrame containing the data.
    """
    folder_path = Path(folder_path)
    file_path = folder_path / file_name
    print(f"Loading Parquet data from: {file_path}")
    LOGGER.info(f"Loading Parquet data from {file_path}")
    try:
        df = pd.read_parquet(file_path)
        # check if the DataFrame is empty
        if df.empty:
            LOGGER.warning("The DataFrame is empty after loading Parquet data.")
            raise ValueError("The DataFrame is empty after loading Parquet data.")
        # check for null values
        if df.isnull().values.any():
            LOGGER.warning("The DataFrame contains null values.")
        # check data types
        if not all(df.dtypes == 'float64'):
            LOGGER.warning("The DataFrame does not contain all float64 data types.")

        print(f"Parquet data loaded successfully with shape {df.shape}")    
        LOGGER.info(f"Parquet data loaded successfully with shape {df.shape}")
        return df
    except Exception as e:
        LOGGER.error(f"Error loading Parquet data: {e}")
        raise

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
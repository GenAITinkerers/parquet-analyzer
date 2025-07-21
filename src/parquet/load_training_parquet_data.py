"""
Load training data for machine learning model.
This read data from from a file in specified folder path and returns it as a pandas DataFrame.
"""

# in build
import logging
import pandas as pd
from pathlib import Path
import json
import os

# user defined
from parquet.util import setup_logger

setup_logger()
LOGGER = logging.getLogger(__name__)

def load_training_data(folder_path: Path | str, file_name: str) -> pd.DataFrame:
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

    # Basic validation checks
    try:
        # Check if the file exists
        if not file_path.exists():
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        # Check if the file is not empty
        if os.stat(file_path).st_size == 0:
            raise ValueError(f"The file {file_path} is empty.")
        
        # Check if the file is readable
        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"The file {file_path} is not readable.")
        
        # Validate file extension
        if file_path.suffix != ".parquet":
            raise ValueError(f"Unsupported file format: {file_path.suffix}. Expected .parquet.")
        
        # Load the data
        df = pd.read_parquet(file_path)

        # Check if the DataFrame is empty
        if df.empty:
            LOGGER.warning("The DataFrame is empty after loading data.")
            raise ValueError(f"The file {file_path} contains no data.")
        
        # Check for null values
        if df.isnull().values.any():
            LOGGER.warning("The DataFrame contains null values.")
            raise ValueError(f"The file {file_path} contains null values.")
        
        # Validate expected columns
        expected_columns = ["column1", "column2", "column3"]  # Replace with actual expected columns
        missing_columns = [col for col in expected_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"The file {file_path} is missing expected columns: {missing_columns}")
        
        # Check for duplicate rows
        if df.duplicated().any():
            LOGGER.warning("The DataFrame contains duplicate rows.")
            raise ValueError(f"The file {file_path} contains duplicate rows.")
        
        # Save feature names for validation
        feature_names = df.columns.tolist()
        feature_file_path = folder_path / "feature_names.json"
        with open(feature_file_path, "w") as f:
            json.dump(feature_names, f)
        LOGGER.info(f"Feature names saved to {feature_file_path}")
        
        LOGGER.info(f"Data loaded successfully with shape {df.shape}")
        return df
    except Exception as e:
        LOGGER.error(f"Error loading data from {file_path}: {e}")
        raise
    finally:
        if 'df' in locals():
            LOGGER.debug(f"Data loaded from {file_path} with columns: {df.columns.tolist()}")
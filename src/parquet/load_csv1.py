"""
Load training data for machine learning model.
This read data from from a file in specified folder path and returns it as a pandas DataFrame.
"""

# in build
import logging
import pandas as pd
from pathlib import Path

# user defined
# from parquet.util import setup_logger
from util import setup_logger



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
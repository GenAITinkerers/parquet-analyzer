import pandas as pd
import os


def load_parquet_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from a Parquet file with basic validation.

    Args:
        file_path (str): Path to the Parquet file.

    Returns:
        pd.DataFrame: Loaded DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or contains null values.
        PermissionError: If the file is not readable.
    """
    import pandas as pd
    import os

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")

    # Check if file is not empty
    if os.stat(file_path).st_size == 0:
        raise ValueError(f"{file_path} is empty.")

    # Check if file is readable
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"{file_path} is not readable.")

    # Check file extension
    if not file_path.endswith(".parquet"):
        raise ValueError(f"{file_path} is not a Parquet file.")

    # Load data
    df = pd.read_parquet(file_path)

    # Check if DataFrame is empty
    if df.empty:
        raise ValueError(f"{file_path} contains no data.")

    # Check for null values
    if df.isnull().values.any():
        raise ValueError(f"{file_path} contains null values.")

    return df

if __name__ == "__main__":
    # Example usage
    file_path = "data/processed/training_data.parquet"
    try:
        df = load_parquet_data(file_path)
        print(f"Data loaded successfully with shape {df.shape}")
    except Exception as e:
        print(f"Error loading data: {e}")

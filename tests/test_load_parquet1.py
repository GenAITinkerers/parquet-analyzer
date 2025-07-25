import pytest
import pandas as pd
import os
from pathlib import Path
from parquet.load_parquet1 import load_parquet_data

@pytest.fixture
def valid_parquet_file(tmp_path):
    """Fixture to create a valid Parquet file."""
    file_path = tmp_path / "valid_data.parquet"
    df = pd.DataFrame({"column1": [1, 2, 3], "column2": [4, 5, 6]})
    df.to_parquet(file_path)
    return file_path

@pytest.fixture
def empty_parquet_file(tmp_path):
    """Fixture to create an empty Parquet file."""
    file_path = tmp_path / "empty_data.parquet"
    pd.DataFrame().to_parquet(file_path)
    return file_path

def test_file_not_found(tmp_path):
    """Test that FileNotFoundError is raised when the file does not exist."""
    non_existent_file = tmp_path / "non_existent.parquet"
    with pytest.raises(FileNotFoundError, match=f"{non_existent_file} does not exist."):
        load_training_data(tmp_path, "non_existent.parquet")

def test_file_not_readable(valid_parquet_file):
    """Test that PermissionError is raised when the file is not readable."""
    with patch("os.access", return_value=False):
        with pytest.raises(PermissionError, match=f"{valid_parquet_file} is not readable."):
            load_training_data(valid_parquet_file.parent, valid_parquet_file.name)

def test_file_empty(empty_parquet_file):
    """Test that ValueError is raised when the file is empty."""
    with pytest.raises(ValueError, match=f"{empty_parquet_file} is empty."):
        load_training_data(empty_parquet_file.parent, empty_parquet_file.name)

def test_file_not_parquet(tmp_path):
    """Test that ValueError is raised when the file is not a Parquet file."""
    non_parquet_file = tmp_path / "data.txt"
    non_parquet_file.write_text("This is not a Parquet file.")
    with pytest.raises(ValueError, match=f"{non_parquet_file} is not a Parquet file."):
        load_training_data(tmp_path, "data.txt")

def test_dataframe_empty_after_loading(empty_parquet_file):
    """Test that ValueError is raised when the DataFrame is empty after loading."""
    with pytest.raises(ValueError, match=f"{empty_parquet_file} contains no data."):
        load_training_data(empty_parquet_file.parent, empty_parquet_file.name)

def test_dataframe_contains_null_values(tmp_path):
    """Test that ValueError is raised when the DataFrame contains null values."""
    file_path = tmp_path / "data_with_nulls.parquet"
    df = pd.DataFrame({"column1": [1, None, 3], "column2": [4, 5, None]})
    df.to_parquet(file_path)
    with pytest.raises(ValueError, match=f"{file_path} contains null values."):
        load_training_data(file_path.parent, file_path.name)

def test_valid_parquet_file(valid_parquet_file):
    """Test that a valid Parquet file is loaded successfully."""
    df = load_training_data(valid_parquet_file.parent, valid_parquet_file.name)
    assert not df.empty
    assert list(df.columns) == ["column1", "column2"]
    assert df.shape == (3, 2)
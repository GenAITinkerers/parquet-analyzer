import pytest
import pandas as pd
from pathlib import Path
from parquet.load_parquet1 import load_parquet_data
import os

# Fixtures and temp files
@pytest.fixture
def sample_parquet_file(tmp_path):
    """Creates a sample valid Parquet file"""
    df = pd.DataFrame({'A': [1, 2], 'B': ['x', 'y']})
    file_path = tmp_path / "valid.parquet"
    df.to_parquet(file_path)
    return tmp_path, "valid.parquet"

@pytest.fixture
def empty_parquet_file(tmp_path):
    """Creates an empty Parquet file"""
    df = pd.DataFrame()
    file_path = tmp_path / "empty.parquet"
    df.to_parquet(file_path)
    return tmp_path, "empty.parquet"

@pytest.fixture
def null_parquet_file(tmp_path):
    """Creates a Parquet file with null values"""
    df = pd.DataFrame({'A': [1, None], 'B': ['x', 'y']})
    file_path = tmp_path / "nulls.parquet"
    df.to_parquet(file_path)
    return tmp_path, "nulls.parquet"

def test_valid_parquet(sample_parquet_file):
    folder, fname = sample_parquet_file
    df = load_parquet_data(folder, fname)
    assert not df.empty
    assert df.shape == (2, 2)

def test_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_parquet_data(tmp_path, "missing.parquet")

def test_non_parquet_file(tmp_path):
    txt_file = tmp_path / "not_parquet.txt"
    txt_file.write_text("This is not a parquet file.")
    with pytest.raises(ValueError, match="not a Parquet file"):
        load_parquet_data(tmp_path, "not_parquet.txt")

def test_empty_file(empty_parquet_file):
    folder, fname = empty_parquet_file
    with pytest.raises(ValueError, match="contains no data"):
        load_parquet_data(folder, fname)

def test_file_with_nulls(null_parquet_file):
    folder, fname = null_parquet_file
    with pytest.raises(ValueError, match="contains null values"):
        load_parquet_data(folder, fname)

def test_unreadable_file(tmp_path):
    unreadable = tmp_path / "unreadable.parquet"
    df = pd.DataFrame({'A': [1]})
    df.to_parquet(unreadable)
    os.chmod(unreadable, 0o000)  # No permissions
    try:
        with pytest.raises(PermissionError):
            load_parquet_data(tmp_path, "unreadable.parquet")
    finally:
        # Reset permissions to allow cleanup
        os.chmod(unreadable, 0o644)

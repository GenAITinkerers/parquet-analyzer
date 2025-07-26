import pytest
import pandas as pd
import os
from pathlib import Path
from parquet.load_parquet1 import load_parquet_data

@pytest.fixture
def tmp_parquet(tmp_path):
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    file_path = tmp_path / "test.parquet"
    df.to_parquet(file_path)
    return tmp_path, "test.parquet"

def test_load_valid_parquet(tmp_parquet):
    folder, fname = tmp_parquet
    df = load_parquet_data(folder, fname)
    assert not df.empty
    assert list(df.columns) == ['a', 'b']

def test_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_parquet_data(tmp_path, "missing.parquet")

def test_empty_file(tmp_path):
    file_path = tmp_path / "empty.parquet"
    file_path.write_bytes(b"")
    with pytest.raises(ValueError, match="is empty"):
        load_parquet_data(tmp_path, "empty.parquet")

def test_not_readable(tmp_parquet):
    folder, fname = tmp_parquet
    file_path = folder / fname
    os.chmod(file_path, 0o000)
    try:
        with pytest.raises(PermissionError):
            load_parquet_data(folder, fname)
    finally:
        os.chmod(file_path, 0o644)

def test_wrong_extension(tmp_path):
    file_path = tmp_path / "test.txt"
    df = pd.DataFrame({'a': [1]})
    df.to_csv(file_path)
    with pytest.raises(ValueError, match="not a Parquet file"):
        load_parquet_data(tmp_path, "test.txt")

def test_null_values(tmp_path):
    df = pd.DataFrame({'a': [1, None]})
    file_path = tmp_path / "nulls.parquet"
    df.to_parquet(file_path)
    with pytest.raises(ValueError, match="contains null values"):
        load_parquet_data(tmp_path, "nulls.parquet")

def test_empty_dataframe(tmp_path):
    df = pd.DataFrame({'a': []})
    file_path = tmp_path / "empty_df.parquet"
    df.to_parquet(file_path)
    with pytest.raises(ValueError, match="contains no data"):
        load_parquet_data(tmp_path, "empty_df.parquet")
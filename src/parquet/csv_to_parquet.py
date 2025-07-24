import pandas as pd

def csv_to_parquet(csv_path, parquet_path, engine='pyarrow'):
    """
    Converts a CSV file to a Parquet file.

    Args:
        csv_path (str): Path to the input CSV file.
        parquet_path (str): Path to the output Parquet file.
        engine (str): Parquet engine ('pyarrow' or 'fastparquet').
    """
    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path, engine=engine)
    print(f"Converted {csv_path} to {parquet_path}")


if __name__ == "__main__":
    # import argparse

    # parser = argparse.ArgumentParser(description="Convert CSV to Parquet")
    # parser.add_argument("csv_path", type=str, help="Path to the input CSV file")
    # parser.add_argument("parquet_path", type=str, help="Path to the output Parquet file")
    # parser.add_argument("--engine", type=str, default='pyarrow', choices=['pyarrow', 'fastparquet'], help="Parquet engine to use")

    # # args = parser.parse_args()
    # # csv_to_parquet(args.csv_path, args.parquet_path, engine=args.engine)
    
    csv_to_parquet("data/raw/training_data.csv", "data/processed/training_data.parquet")

    df = pd.read_parquet("data/processed/training_data.parquet")
    print(df.head())
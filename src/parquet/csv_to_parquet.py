import pandas as pd

# Step 1: Read CSV file
csv_file_path = "artifacts/input/training_data_for_parquet.csv"
df = pd.read_csv(csv_file_path)
print(df.head())  # Display the first few rows of the DataFrame

# Step 2: Write to Parquet file
parquet_file_path = "artifacts/input/training_data.parquet"
df.to_parquet(parquet_file_path, engine='pyarrow')  # or engine='fastparquet'

print(f"CSV file converted to Parquet and saved at: {parquet_file_path}")

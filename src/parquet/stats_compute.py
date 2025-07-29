from parquet.load_parquet import load_parquet_data
import os
import pandas as pd


# Load the Parquet file and compute statistics

def stats_pipeline(
        input_path: str = 'data/processed/', 
        stats_path: str = 'data/output'
        ):
    """
    Load the Parquet file and compute statistics.
    
    Returns:
        pd.DataFrame: DataFrame containing the computed statistics.
    """

    file_name = 'training_data.parquet'
    df = load_parquet_data(input_path, file_name)
    
    stats = df.describe()
    stats.drop(['time', 'TO'], axis=1, inplace=True)

    print(stats)

    save_statistics_to_csv(stats, stats_path)
    print("Statistics computed and saved successfully.")




def save_statistics_to_csv(stats: pd.DataFrame, stats_path: str):
    """
    Save the computed statistics to a CSV file.
    
    Args:
        stats (pd.DataFrame): DataFrame containing the computed statistics.
        output_file (str): Path to the output CSV file.
    """
    output_file = os.path.join(stats_path, 'statistics.csv')
    print(f"Saving statistics to {output_file}")
    stats.to_csv(output_file)


def main():
    """
    Main function to execute the statistics pipeline.
    """
    input_path = os.getenv('INPUT_PATH', 'data/processed/')
    stats_path = os.getenv('STATS_PATH', 'data/output')
    stats_pipeline(input_path, stats_path)


if __name__ == "__main__":
    main()
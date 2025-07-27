from load_parquet import load_parquet_data

folder = 'data/processed/'
file_name = 'training_data.parquet'
df = load_parquet_data(folder, file_name)

print(df.head())

stats = df.describe()
stats.drop(['time', 'TO'], axis=1, inplace=True)

print(stats)
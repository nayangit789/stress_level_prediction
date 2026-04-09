import pandas as pd

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
    print(df.info())
    return df
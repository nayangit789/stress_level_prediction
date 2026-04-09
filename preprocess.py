import pandas as pd
def preprocess_data(df):
    print("Preprocessing data...")

    # handel the misssing values
    df = df.dropna()

    #encode the categorical values to numerics
    df = pd.get_dummies(df, drop_first= True)
    return df
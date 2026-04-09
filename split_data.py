from sklearn.model_selection import train_test_split
def split_data(df):
    print("Splitting data into train and test sets...")
    X = df.drop('Stress_Level', axis=1)
    y = df['Stress_Level']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
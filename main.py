# main.py

from load_dataset import load_dataset
from preprocess import preprocess_data
from split_data import split_data
from train import train_model
from evaluate import evaluate_model

# Step 1: Load Data
df = load_dataset("stress_dataset.csv")

# Step 2: Preprocess
df = preprocess_data(df)

# Step 3: Split
X_train, X_test, y_train, y_test = split_data(df)

# Step 4: Train
model = train_model(X_train, y_train)

# Step 5: Evaluate
evaluate_model(model, X_test, y_test)
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

def train_model():
    # Load and process data
    heart_data = pd.read_csv('heart_disease_data.csv')
    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    # Train model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, Y_train)

    # Save model
    with open('heart_disease_model.pkl', 'wb') as file:
        pickle.dump(model, file)

def predict(input_data):
    with open('heart_disease_model.pkl', 'rb') as file:
        model = pickle.load(file)
    input_data_np = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_data_np)
    return prediction[0]

if __name__ == "__main__":
    train_model()

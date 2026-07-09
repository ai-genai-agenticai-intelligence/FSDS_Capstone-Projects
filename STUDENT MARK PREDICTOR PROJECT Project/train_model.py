import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import os

def train():
    data_path = 'student_info.csv'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return
    
    df = pd.read_csv(data_path)
    df['study_hours'] = df['study_hours'].fillna(df['study_hours'].mean())
    X = df[['study_hours']]
    y = df['student_marks']
    
    model = LinearRegression()
    model.fit(X, y)
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model trained and saved.")

if __name__ == "__main__":
    train()

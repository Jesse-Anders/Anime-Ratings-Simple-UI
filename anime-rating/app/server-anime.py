from fastapi import FastAPI
import joblib
import numpy as np

# Load the anime model
model = joblib.load('app/anime_model.joblib')

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Anime model API'}

@app.post('/predict')
def predict(data: dict):
    """
    Predicts the Anime Rating.

    Args:
        data (dict): A dictionary containing the features to predict.
        Anime Rating Has 40 Features
        e.g. {"features": [1, 2, 3, 4]}

    Returns:
        dict: A dictionary containing the predicted rating.
    """        
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)[0]  # Obtain numerical output
    return {'predicted_rating': float(prediction)}  # Convert prediction to float if needed
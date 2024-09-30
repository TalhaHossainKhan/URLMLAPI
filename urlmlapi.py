from fastapi import FastAPI
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

@app.get("/")
async def gatherPredict_data(URL: str):
    # Load the pre-trained model and vectorizer from a pickle file
    with open('url_model.pkl', 'rb') as f:
        model, vectorizer = pickle.load(f)

    # Transform the input URL into a feature vector using the loaded vectorizer
    prediction_data = pd.DataFrame.sparse.from_spmatrix(vectorizer.transform([URL]), columns=vectorizer.get_feature_names_out())
    Predict = model.predict(prediction_data)

    #Return prediction
    return {"Prediction": int(Predict[0])}

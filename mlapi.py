from fastapi import FastAPI
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

@app.get("/")
async def gatherPredict_data(URL: str):
    with open('url_model.pkl', 'rb') as f:
        model, vectorizer = pickle.load(f)

    prediction_data = pd.DataFrame.sparse.from_spmatrix(vectorizer.transform([URL]), columns=vectorizer.get_feature_names_out())
    Predict = model.predict(prediction_data)

    return {"Prediction: ": int(Predict)}

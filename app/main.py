from fastapi import FastAPI
import pandas as pd
import joblib

from app.schema import DeliveryInput

app = FastAPI()

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("artifacts/model.pkl")


@app.get("/")
def home():
    return {"message": "Delivery Time Prediction API Running"}


@app.post("/predict")
def predict(data: DeliveryInput):

    # Convert input → dict → DataFrame
    input_dict = data.model_dump()
    df = pd.DataFrame([input_dict])

    # Prediction
    prediction = model.predict(df)[0]

    return {
        "predicted_delivery_time": round(prediction, 2)
    }
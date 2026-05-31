import json
import numpy as np
import pandas as pd
import xgboost as xgb
import lightgbm as lgb
import tensorflow as tf

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# LOAD XGBOOST
xgb_model = xgb.XGBClassifier()
xgb_model.load_model("xgb_model.json")

# LOAD LIGHTGBM
lgbm_model = lgb.Booster(model_file="lgbm_model.txt")

# LOAD NEURAL NETWORK
nn_model = tf.keras.models.load_model("nn_model.keras")

# LOAD SCALER JSON
with open("scaler.json", "r") as f:
    scaler_data = json.load(f)

mean = np.array(scaler_data["mean"])
scale = np.array(scaler_data["scale"])

# LOAD WEIGHTS JSON
with open("weights.json", "r") as f:
    weights_data = json.load(f)

w = np.array(weights_data["weights"])

# LABEL
label_map = {
    0: "Introvert",
    1: "Ekstrovert",
    2: "Ambivert"
}

# FEATURE COLUMNS
COLUMNS = ["gender", "age"] + [f"Q{i}A" for i in range(1, 92)]

# REQUEST BODY
class PredictRequest(BaseModel):
    gender: int
    age: int
    answers: list[int]

# HOME
@app.get("/")
def home():
    return {"message": "API ACTIVE"}

# PREDICT
@app.post("/predict")
def predict(data: PredictRequest):

    row = [data.gender, data.age] + data.answers

    df = pd.DataFrame([row], columns=COLUMNS)

    # manual scaling
    X = (df.values - mean) / scale

    # predict
    p1 = xgb_model.predict_proba(X)

    p2 = lgbm_model.predict(X)
    p2 = np.array(p2)

    p3 = nn_model.predict(X, verbose=0)

    final = (
        w[0] * p1 +
        w[1] * p2 +
        w[2] * p3
    )

    final = final[0]

    pred = np.argmax(final)

    return {
        "Introvert": float(final[0]),
        "Ekstrovert": float(final[1]),
        "Ambivert": float(final[2]),
        "Prediction": label_map[pred]
    }
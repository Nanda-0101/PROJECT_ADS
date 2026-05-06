import numpy as np
import joblib
import json
from tensorflow import keras

# load model
xgb = joblib.load("xgb_model.pkl")
rf = joblib.load("rf_model.pkl")
nn = keras.models.load_model("nn_model.h5")
scaler = joblib.load("scaler.pkl")

with open("weights.json") as f:
    w = np.array(json.load(f))

label_map = {0:"Introvert",1:"Ekstrovert",2:"Ambivert"}

def predict(input_data):
    x = scaler.transform([input_data])

    p1 = xgb.predict_proba(x)
    p2 = rf.predict_proba(x)
    p3 = nn.predict(x)

    final = w[0]*p1 + w[1]*p2 + w[2]*p3
    pred = np.argmax(final)

    return label_map[pred], final[0].tolist()

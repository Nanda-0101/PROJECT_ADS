import requests

HF_SPACE_URL = "https://nanda010101-intro-ekstro-ambi.hf.space/predict"

def predict_kepribadian(gender, age, jawaban):
    response = requests.post(
        HF_SPACE_URL,
        json={
            "gender": gender,
            "age": age,
            "answers": jawaban
        },
        timeout=600
    )
    
    response.raise_for_status()
    
    data = response.json()
    
    # Return prediction and probabilities
    return data["Prediction"], {
        "Introvert": data["Introvert"],
        "Ekstrovert": data["Ekstrovert"],
        "Ambivert": data["Ambivert"]
    }
import requests

HF_SPACE_URL = "https://nanda010101-intro-ekstro-ambi.hf.space/predict"

def predict_kepribadian(gender, age, jawaban):

    try:

        response = requests.post(
            HF_SPACE_URL,
            json={
                "gender": gender,
                "age": age,
                "answers": jawaban
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data["Prediction"]

    except Exception as e:

        print("HF ERROR:", str(e))

        return "Ambivert"
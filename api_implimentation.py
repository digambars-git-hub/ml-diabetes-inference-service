import requests

API_URL = "http://127.0.0.1:8000/diabetes_prediction"

input_data_for_model = {
    "Pregnancies": 1,
    "Glucose": 85,
    "BloodPressure": 66,
    "SkinThickness": 29,
    "Insulin": 0,
    "BMI": 26.6,
    "DiabetesPedigreeFunction": 0.351,
    "Age": 35,
}


def main():
    try:
        response = requests.post(API_URL, json=input_data_for_model, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
        return

    print(response.json())


if __name__ == "__main__":
    main()

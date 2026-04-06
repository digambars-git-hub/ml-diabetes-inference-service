from fastapi.testclient import TestClient

from ml_api import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"


def test_prediction_response_schema():
    payload = {
        "Pregnancies": 1,
        "Glucose": 85,
        "BloodPressure": 66,
        "SkinThickness": 29,
        "Insulin": 0,
        "BMI": 26.6,
        "DiabetesPedigreeFunction": 0.351,
        "Age": 35,
    }
    response = client.post("/diabetes_prediction", json=payload)
    assert response.status_code == 200

    body = response.json()
    assert set(body.keys()) == {"prediction", "result"}
    assert body["prediction"] in {0, 1}
    assert isinstance(body["result"], str)

from pathlib import Path
import pickle

from fastapi import FastAPI
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "diabetes_model.sav"

app = FastAPI(
    title="Diabetes Prediction API",
    description="FastAPI service for diabetes prediction using a trained scikit-learn model.",
    version="1.0.0",
)


class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


def load_model(model_path: Path):
    with model_path.open("rb") as model_file:
        return pickle.load(model_file)


diabetes_model = load_model(MODEL_PATH)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Diabetes Prediction API is running."}


@app.post("/diabetes_prediction")
def diabetes_pred(input_parameters: ModelInput):
    input_list = [
        input_parameters.Pregnancies,
        input_parameters.Glucose,
        input_parameters.BloodPressure,
        input_parameters.SkinThickness,
        input_parameters.Insulin,
        input_parameters.BMI,
        input_parameters.DiabetesPedigreeFunction,
        input_parameters.Age,
    ]

    prediction = int(diabetes_model.predict([input_list])[0])
    result = "The person is not Diabetic." if prediction == 0 else "The person is Diabetic."

    return {"prediction": prediction, "result": result}

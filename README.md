# Diabetes Prediction API

FastAPI service that loads a trained scikit-learn model (`diabetes_model.sav`) and exposes a REST endpoint for diabetes prediction.

## What each file does

- `ml_api.py`: Main FastAPI app, input schema validation, model loading, and prediction endpoint.
- `api_implimentation.py`: Small client script that sends a sample request to the API.
- `diabetes_model.sav`: Pickled trained model used for inference.
- `requirements.txt`: Python dependencies needed to run the API and sample client.
- `.gitignore`: Files and folders that should not be committed to Git.
- `LICENSE`: Open-source license for repository usage.

## Quick start

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run the API server.
4. Call the API using the sample script.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn ml_api:app --reload
```

In another terminal:

```bash
python api_implimentation.py
```

## Run tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## API details

- Endpoint: `POST /diabetes_prediction`
- Input JSON:

```json
{
  "Pregnancies": 1,
  "Glucose": 85,
  "BloodPressure": 66,
  "SkinThickness": 29,
  "Insulin": 0,
  "BMI": 26.6,
  "DiabetesPedigreeFunction": 0.351,
  "Age": 35
}
```

- Response JSON:

```json
{
  "prediction": 0,
  "result": "The person is not Diabetic."
}
```

Interactive docs are available at:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Model/version note

This model artifact was originally created with an older scikit-learn version. If you see version warnings during model load, retraining and re-saving the model in your current environment is the best long-term fix.

## CI

GitHub Actions workflow is included at `.github/workflows/ci.yml` and runs tests on every push and pull request.

from fastapi import FastAPI
from pydantic import BaseModel
from model import SimpleModel


app = FastAPI()

model = SimpleModel()

class InputData(BaseModel):
    value: float

## read request

@app.get("/")
def read_root():
    return {"message" : "Model API is up and running "}


@app.post("/predict")
def predict(data:InputData):
    result = model.predict(data.value)
    return {
        "input":data.value,
        "prediction": result
    }

from fastapi import FastAPI, Form
from pydantic import BaseModel
#from typing import Annotated
from typing_extensions import Annotated
from sklearn.pipeline  import Pipeline
import pandas as pd


from passenger_transformer import PassengerTransformer


import joblib

loaded_model = joblib.load("rf_model.joblib")

app = FastAPI()


class Person(BaseModel):


    #username: str
    #password: str
    Pclass : int
    Sex: str
    Age : float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str

    #==========================================


@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": loaded_model is not None}
    
@app.post("/predict/")
async def predict(person: Annotated[Person, Form()]):
    print()
   
    print()
    dumped_data = person.model_dump()

# 2. Pass it as a list to the DataFrame constructor
    df = pd.DataFrame([dumped_data])
    print()
    predictions = loaded_model.predict(df)
    print("predictions")
    print(predictions)
    print()
    probs=loaded_model.predict_proba(df)

    print("probs:", probs)
    print("probs shape:", probs.shape)

    print()
    #print (df)
    print()

    
    #return {"survived": int(predictions[0]), "probability": probs[[0,0]]}
    return {"survived": int(predictions[0]), "survival_probability": float(probs[0,1])}

   



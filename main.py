import os
from dotenv import load_dotenv
from fastapi import FastAPI, status, HTTPException

import auth
from fastapi.middleware.cors import CORSMiddleware
from models import PredictionData, pred_colmn, LoanApproval
import pickle
import pandas as pd

app = FastAPI()
app.include_router(auth.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

loan_model=pickle.load(open('loan_prediction_model.sav', 'rb'))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/creditapproval", status_code=status.HTTP_200_OK)
async def credit_card_approval_prediction(predictiondata: PredictionData):
    return {"approval" : 'Yes'}

@app.post("/loanapproval", status_code=status.HTTP_200_OK)
async def loan_approval_prediction(loanapproval: LoanApproval):
    loanapproval=loanapproval.dict()
    loanapproval['Loan_ID']='LP001015'
    input_data=pd.DataFrame(loanapproval.values(), loanapproval.keys()).T
    prediction=loan_model.predict(input_data)[0]
    if prediction==1:
        prediction='Yes'
    else:
        prediction='No'
    return {"approval": prediction}

@app.post("/mfadvisor", status_code=status.HTTP_200_OK)
async def mutual_funds_investment_advisor():
    advice="idiot"
    return {"advice": advice}

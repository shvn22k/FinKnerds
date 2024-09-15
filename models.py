from dataclasses import Field
from typing import Literal, Optional

from pydantic import BaseModel, conint, validator, confloat

pred_colmn = ['Gender', 'Reality', 'ChldNo_1', 'ChldNo_2More', 'wkphone',
              'gp_Age_high', 'gp_Age_highest', 'gp_Age_low', 'gp_Age_lowest',
              'gp_worktm_high', 'gp_worktm_highest', 'gp_worktm_low',
              'gp_worktm_medium', 'occyp_hightecwk', 'occyp_officewk', 'famsizegp_1',
              'famsizegp_3more', 'houtp_Co-op apartment', 'houtp_Municipal apartment',
              'houtp_Office apartment', 'houtp_Rented apartment',
              'houtp_With parents', 'edutp_Higher education',
              'edutp_Incomplete higher', 'edutp_Lower secondary',
              'famtp_Civil marriage', 'famtp_Separated', 'famtp_Single / not married',
              'famtp_Widow']


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    location: Optional[str] = None
    country_code: Optional[str] = None


class UpdateUser(BaseModel):
    email: Optional[str] = None
    location: Optional[str] = None
    country_code: Optional[str] = None


class CreateUserRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    location: str
    country_code: str
    gender: Literal['male', 'female']


class OpenAIData(BaseModel):
    data1: dict


class UserData(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    gender: Literal['male', 'female']
    location: str
    country_code: str


class PredictionData(BaseModel):
    Gender: float
    Reality: float
    ChldNo_1: float
    ChldNo_2More: float
    wkphone: float
    gp_Age_high: float
    gp_Age_highest: float
    gp_Age_low: float
    gp_Age_lowest: float
    gp_worktm_high: float
    gp_worktm_highest: float
    gp_worktm_low: float
    gp_worktm_medium: float
    occyp_hightecwk: float
    occyp_officewk: float
    famsizegp_1: float
    famsizegp_3more: float
    houtp_Co_op_apartment: float
    houtp_Municipal_apartment: float
    houtp_Office_apartment: float
    houtp_Rented_apartment: float
    houtp_With_parents: float
    edutp_Higher_education: float
    edutp_Incomplete_higher: float
    edutp_Lower_secondary: float
    famtp_Civil_marriage: float
    famtp_Separated: float
    famtp_Single_not_married: float
    famtp_Widow: float

    @validator('Gender', pre=True)
    def convert_gender_to_float(cls, value):
        gender_mapping = {'male': 0.0, 'female': 1.0}
        if isinstance(value, str) and value.lower() in gender_mapping:
            return gender_mapping[value.lower()]
        raise ValueError('Invalid gender value. Expected "male" or "female".')

class LoanApproval(BaseModel):
        #Loan_ID='LP001015'
        Gender: Literal['Male', 'Female']
        Married: Literal['Yes', 'No']
        Dependents: Literal["0", "1", "2", "3+"]
        Education: Literal["Graduate", "Not Graduate"]
        Self_Employed: Literal['Yes', 'No']
        ApplicantIncome: conint(ge=100)
        CoapplicantIncome: confloat(ge=90)
        LoanAmount: confloat(ge=1000)
        Loan_Amount_Term: confloat(ge=10)
        Credit_History: float
        Property_Area: Literal["Urban", "Rural", "Semiurban"]

class MFAdvisor(BaseModel):
    fund_name: str

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # now we will use field_validator to add custom validation logic, for example, we will validate whether the email of the patient belongs to a specific domain or not like hdfc.com or icici.com
    # to do this, we will have to create a method with @field_validator decorator and provide the field name which we want to validate, in this case, it is email
    @field_validator('email')
    @classmethod  # this line tells that the method is a class method and not an instance method
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        # Check if the email domain is either hdfc.com or icici.com
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain, Email must belong to either hdfc.com or icici.com")
        return value

    @field_validator('age')
    @classmethod
    def age_validator(cls, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        return value
    

@field_validator('weight')
@classmethod
def weight_validator(cls, value):
    if value < 0:
        raise ValueError("Weight cannot be negative")
    return value

@field_validator('name')
@classmethod
def transform_name(cls, value):
    return value.upper()

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}


patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)

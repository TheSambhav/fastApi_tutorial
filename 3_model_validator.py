from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]



    #  model validator to validate the entire model after all field validations are done, 
    # we will check if the patient is older than 60 years, then the contact_details must contain an emergency contact number
    # which means that we are validating multiple fields together, so we will use model_validator here not the field_validator
  
  
    @model_validator(mode='after') # here we are not specifying any field name because we are validating the entire model, we just set mode to 'after' to indicate that this validation should happen after all field validations are done
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

# function to demonstrate the usage of the Patient model
# this function takes a Patient instance as input and prints some of its attributes
# this function can be used to show how the model works and how the validations are applied


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462' , 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)


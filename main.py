from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated    , Literal

import json


app = FastAPI()



class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Unique identifier for the patient")]
    name: Annotated[str, Field(..., description=  "Name of the patient")]
    city: Annotated[str, Field(..., description="City of the patient")]
    age: Annotated[int, Field(..., description="Age of the patient")]
    gender: Annotated[str, Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., description="Height of the patient in cm")]
    weight: Annotated[float, Field(..., description="Weight of the patient in kg")]
    
    @computed_field
    @property   
    def bmi(self) -> float:
        bmi = round(self.weight/((self.height/100)**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'underweight'
        elif 18.5 <= self.bmi < 24.9:
            return 'normal'
        elif 25 <= self.bmi < 29.9:
            return 'overweight'
        else:
            return 'obese'


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data 
   
# we will create a utility function save_data to save the updated patient data back to the JSON file.
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data,f)


@app.get("/")

def hello():
    return {'message': 'Hello world!'} 


@app.get("/about")
def about():
    return {'message': 'This is a FastAPI practise project.'}     


@app.get("/contact")
def contact():
    return {'message': 'Contact us at contact@example.com'}

@app.get("/help")
def help():
    return {'message': 'For help, visit our help center at help.example.com'}


@app.get("/status" )
def status():
    return {'message': 'Server is running successfully'}


@app.get('/view')
def view():
    data = load_data()
    return data    


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='Id of the patient in the db', examples='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')    



# here we will create an endpoint to sort patients based on a specific field like height, weight, or bmi, and also allow the user to specify the order of sorting (ascending or descending) using query parameters.
# we have used path parameters and query parameters in this endpoint.
#  path parameters are used to identify a specific resource, in this case, the patient_id, while query parameters are used to filter or sort the data returned by the endpoint.
# for example, in this endpoint, the path parameter patient_id is used to identify a specific patient, while the query parameters sort_by and order are used to sort the list of patients based on the specified field and order.
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='sort on the basis of height weight or bmi'),
                   order: str = Query('asc', description = 'sort in asc or desc order')):
    valid_feilds = ['height','weight','bmi']

    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400, detail=f'Invalid feild, select from {valid_feilds}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Order must be asc or desc')
    data = load_data()

    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by,0) ,reverse= sort_order)
    return sorted_data

# here we have created multiple endpoints to demonstrate the usage of FastAPI, including path parameters and query parameters.
# query parameters are optional parameters that can be added to the URL to filter or sort the data, while path parameters are required parameters that are part of the URL path itself.




# now we will create an endpoint named create_patient to demonstrate how to create a new patient record using a POST request.

# client will send an HTTP POST request to the /create_patient endpoint with the patient data in the request body, and the server will process this data to create a new patient record.
# a request body is the data sent by the client to the server when making a POST request, typically in JSON format, containing the information needed to create or update a resource on the server.
# to validate and parse the data sent in the request body by the client, we will use Pydantic models, which allow us to define the structure and types of the data we expect to receive.


@app.post('/create_patient')
def create_patient(patient:Patient):

    # load the existing data from the JSON file

    data = load_data() 


    # check if the patient ID already exists in the data

    if patient.id in data:
       raise HTTPException(status_code=400, detail='Patient with this ID already exists')

    # new patient data to be added

    # first we need to convert the Pydantic model instance to a dictionary using the model_dump() method, which serializes the model into a dictionary format.
    data[patient.id] = patient.model_dump(exclude=['id'])


    # save the updated data back to the JSON file
    save_data(data)

    return JSONResponse(status_code= 201, content= {'message': 'Patient created successfully'})

     
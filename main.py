from fastapi import FastAPI

import json


app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data 
   



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


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error': 'Patient not found'}



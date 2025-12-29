from fastapi import FastAPI, Path, HTTPException, Query

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


@app.get('/view')
def view():
    data = load_data()
    return data    


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='Id of the patient in the db',example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')    



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

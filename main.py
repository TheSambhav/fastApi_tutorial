from fastapi import FastAPI

app = FastAPI()

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
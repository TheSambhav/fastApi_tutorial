# def insert_patient_data(name: str, age: int):
    
#     if type(name) == str and type(age)==int:
#         print(name)
#         print(age)
#         print('inserted successfully')

#     else:
#         raise TypeError('Invalid data types')
    

# def update_patient_data(name: str, age: int):

#     if age < 0:
#         raise ValueError('Age cannot be negative')
    
#     if type(name) == str and type(age)==int:
#         print(name)
#         print(age)
#         print('updated successfully')

#     else:
#         raise TypeError('Invalid data types')    

# insert_patient_data('John Doe', 30)        
 

# to avoid all this TypeError and ValueError handling, we can use Pydantic

from pydantic import BaseModel, EmailStr, AnyUrl, Feild # Feild is used to provide additional custom validation on data accoridng to our needs

from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str  = Feild(min_length=2, max_length=50) # here we are using Feild to provide custom validation that name should be between 2 to 50 characters
    second_name: Annotated[str, Feild(min_length=2, max_length=50, title = 'second_name_of_patient', description = 'Second name of the patient', examples = ['Doe','Malfoy','Potter'])] # here we are using Feild to provide custom validation that second_name should be between 2 to 50 characters
    email: EmailStr # Pydantic provides built-in types for common data types like EmailStr, constr, conint, etc. to perform data validation
    linkedin_url: AnyUrl # to validate URL fields
    age: int
    weight: float = Feild(gt=0, lt = 120) # here we are using Feild to provide custom validation that weight should be greater than 0 and less than 120
    married: bool = False
    allergies: Annotated[Optional[List[str]], Feild(max_length=5)]  # here we are using Feild to provide custom validation that maximum 5 allergies can be provided 
    contacts: Dict[str, str]



    # Feild function is also used to attach metadata to the fields, which can be used in API documentation generation tools like FastAPI
    # We  can do this using Annotated type from typing module with Feild function
    # allergies: Optional[Annotated[List[str], Feild(max_length=5)]]  # here we are using Feild to provide custom validation that maximum 5 allergies can be provided
    #  we can also use Annotated type to provide additional metadata to the fields, like title, description, examples, etc.
    # we can also use Feild function to provide default values to the fields, like married field here, which is set to False by default, the code will look like this married: Annotated[bool, Feild(default=False, description='Marital status of the patient')]



    # generally we use Optional for fields which are not mandatory, all the feilds are mandatory by default, if we don't provide any default value, like married field here, 
    # it will be considered as mandatory field
    #  this was type validation and conversion is done automatically by Pydantic
    # if we use strcit parameter from pydantic, then it will not do any type conversion, it will only validate the data types strictly, for example, if we provide weight as '30' (string), it will raise a validation error, the code will look like this weight: Annotated[float, Feild(strict=True, gt=0, lt=120)]

    # now we try to do data validation with wrong data types by using email example


    

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)  
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)    
    print(patient.contacts)
    print(patient.email)
    print('inserted successfully')

patient_info = {'name': 'John Doe', 'email': 'abc@gmail.com', 'linkedin_url': 'https://www.linkedin.com/in/johndoe', 'age': 30, 'weight': 70.5, 
                'married' : True, 'allergies': ['Peanuts', 'Dust'],
                'contacts': {'email': 'ema@gmail.com', 'phone': '986543210'}}    

patient1 = Patient(**patient_info) 


insert_patient_data(patient1)



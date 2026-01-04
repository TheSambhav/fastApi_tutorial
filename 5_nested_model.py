
from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

    # here address is a nested model of type Address, which means that the address field itself is an instance of the Address model, this allows us to group related fields together and create a hierarchical structure for our data models.
    # for example, the address field contains multiple sub-fields like city, state, and pin, which are all related to the address of the patient. By using a nested model, we can encapsulate these related fields within a single address field, making our data model more organized and easier to manage.
address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include={'address': True})

print(type(temp))























# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed


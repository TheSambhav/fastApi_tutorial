from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)

# model_dump is used to serialize the model into a dictionary format, making it easy to convert to JSON or other formats for storage or transmission.
# exclude_unset=True ensures that only fields that have been explicitly set (i.e., not default values) are included in the output dictionary.
# This is useful for reducing the size of the serialized data and avoiding unnecessary information.
# other than exclude_unset, we can also use include, exclude, by_alias, etc. to customize the serialization process further.
# we also have model_dump_json method to directly serialize the model into a JSON string.
# these serialization features are particularly useful when working with APIs, databases, or any scenario where data needs to be transmitted or stored in a structured format.

print(temp)
print(type(temp))
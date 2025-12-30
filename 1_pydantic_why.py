def insert_patient_data(name: str, age: int):
    
    if type(name) == str and type(age)==int:
        print(name)
        print(age)
        print('inserted successfully')

    else:
        raise TypeError('Invalid data types')
    

def update_patient_data(name: str, age: int):

    if age < 0:
        raise ValueError('Age cannot be negative')
    
    if type(name) == str and type(age)==int:
        print(name)
        print(age)
        print('updated successfully')

    else:
        raise TypeError('Invalid data types')    

insert_patient_data('John Doe', 30)        

from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    name : str
    age : int
    gender : str
    address : Address


def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.gender)
    print(patient.address)
    
    print('inserted successfully')


address_dict = {'city' : 'Pune', 'state' : 'Maharashtra', 'pin' : '413801'}

address1 = Address(**address_dict)

patient_dict = {'name' : 'Rahul', 'age' : 35, 'gender' : 'Male', 'address' : address1}

patient1 = Patient(**patient_dict)


insert_patient_data(patient1)
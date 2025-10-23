from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    name : str
    age : int
    gender : str = 'Male'
    address : Address


def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.gender)
    print(patient.address)
    
    print('inserted successfully')


address_dict = {'city' : 'Pune', 'state' : 'Maharashtra', 'pin' : '413801'}

address1 = Address(**address_dict)

patient_dict = {'name' : 'Rahul', 'age' : 35, 'address' : address1}

patient1 = Patient(**patient_dict)


# temp = patient1.model_dump(include = ['name', 'address'])

temp = patient1.model_dump(exclude = {'address' : ['state']}, exclude_unset = True)

print(temp)
print(type(temp))
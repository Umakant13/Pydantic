from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int
    

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print('inserted successfully')

def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print('updated successfully')

patient_info = {'name' : 'john', 'age' : 30}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)
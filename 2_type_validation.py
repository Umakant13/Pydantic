from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name : str
    age : int
    weight: float
    married : bool = False
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]
    

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    
    print('inserted successfully')

def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print('updated successfully')

patient_info = {'name' : 'john', 'age' : 30, 'weight' : 65.5, 'married' : True, 
                'allergies' : ['pollen', 'dust'], 'contact_details' : {'email' : 'abc@gmail.com', 'phone' : '1234567890'}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)
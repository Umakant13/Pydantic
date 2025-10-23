from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    weight: float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]
    
    @model_validator(mode = 'after')
    def validate_emergency_contact(cls, model):

        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years')
        return model

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    
    print('inserted successfully')


patient_info = {'name' : 'john', 'age' : 65, 'email' : 'abc@hdfc.com', 'weight' : 65.5, 'married' : True, 
                'allergies' : ['pollen', 'dust'], 'contact_details' : {'phone' : '1234567890', 'emergency': '234564933'}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
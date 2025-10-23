from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    weight: float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]
    
    # Validation

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError(f'Email domain must be one of {valid_domains}')
        
        return value
    
    #Transformation

    @field_validator('name', mode = 'after')
    @classmethod
    def name_validator(cls, value):

        return value.upper()

    @field_validator('age', mode = 'before')
    @classmethod
    def age_validator(cls, value):

        if value > 0 and  value < 100:
            return value
        else:
            raise ValueError('Age must be between 1 and 99')

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    
    print('inserted successfully')

def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print('updated successfully')

patient_info = {'name' : 'john', 'age' : 30, 'email' : 'abc@hdfc.com', 'weight' : 65.5, 'married' : True, 
                'allergies' : ['pollen', 'dust'], 'contact_details' : {'phone' : '1234567890'}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : Annotated[str, Field(max_length= 50, title= 'Name of the patient', descrtiption = 'Name should not exceed 50 characters', examples= ['John', 'Alice', 'Bob'])]

    age : int = Field(gt = 0, lt = 70, description= 'Age must be between 1 and 69 years')
    
    email : EmailStr
    linkedin_url : AnyUrl
    
    weight: Annotated[float , Field(gt = 0, description = "Weight must be greater than zero", strict = True)]
    
    married : Annotated[bool, Field(default= None, description= 'Martial Status of the patient')]

    allergies : Annotated[Optional[List[str]] , Field (default= None, max_length = 5)]

    contact_details : Dict[str, str]
    

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    
    print('inserted successfully')

def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print('updated successfully')

patient_info = {'name' : 'john', 'age' : 30, 'email' : 'john@gmail.com','linkedin_url' : 'http://linkedin.com/in/john', 'weight' : 65.5, 'married' : True, 
                'allergies' : ['pollen', 'dust'], 'contact_details' : {'phone' : '1234567890'}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)
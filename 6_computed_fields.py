from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    weight: float
    height: float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @computed_field
    @property
    def BMI(self) -> float:

        bmi = round(self.weight / (self.height **2), 2)
        return bmi
    


def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print('BMI :',patient.BMI)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    
    print('inserted successfully')


patient_info = {'name' : 'john', 'age' : 65, 'email' : 'abc@hdfc.com', 'weight' : 65.5, 'height' : 1.76, 'married' : True, 
                'allergies' : ['pollen', 'dust'], 'contact_details' : {'phone' : '1234567890', 'emergency': '234564933'}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
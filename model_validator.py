from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    age: int=Field(ge=0, lt=100)
    email: EmailStr
    married: bool
    allergies: Annotated[Optional[List[str]], Field(default=None, max_lenght=5)]
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years old')
        return model
    
    


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("updated")

patient_info ={'name':'John Doe', 'age':'65', 'email':'abc@icici.com', 'married':True,
                       'contact_details':{'email':'abc@gmail.com', 'phone':'2353426', 'emergency':'9876543210'}}

patient1=Patient(**patient_info)
update_patient_data(patient1)
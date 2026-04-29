from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    age: int=Field(ge=0, lt=100)
    email: EmailStr
    married: bool
    allergies: Annotated[Optional[List[str]], Field(default=None, max_lenght=5)]
    contact_details: Dict[str,str]


    @field_validator('email')
    @classmethod

    def email_validator(cls, value):
        valid_domains=['hdfc.com','icici.com']
        #abc@gmail.com

        domain=value.split('@')[-1]

        if domain not in valid_domains:
            raise ValueError(f'Email domain must be one of {valid_domains}')
        return value
    
    @field_validator('name',)
    @classmethod
    def tranform_name(cls, value):
        return value.upper()
    
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0<value < 100:
            return value
        else:
            raise ValueError('Age must be between 0 and 100')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("updated")

patient_info ={'name':'John Doe', 'age':'30', 'email':'abc@icici.com', 'married':True,
                       'contact_details':{'email':'abc@gmail.com', 'phone':'2353426'}}

patient1=Patient(**patient_info)
update_patient_data(patient1)
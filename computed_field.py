from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient Name", description="Enetr patient name in less than 50 characters")]
    age: int=Field(ge=0, lt=100)
    weight: float #kgs
    hieght: float #meters
    married: bool
    allergies: Annotated[Optional[List[str]], Field(default=None, max_lenght=5)]
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi=self.weight/(self.hieght**2)
        return round(bmi,2)

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('BMI',patient.bmi)
    print("updated")

patient_info ={'name':'John Doe', 'age':30, 'married':True, 'weight':70.5, 'hieght':1.75,
                       'contact_details':{'email':'abc@gmail.com', 'phone':'2353426'}}

patient1=Patient(**patient_info)
update_patient_data(patient1)
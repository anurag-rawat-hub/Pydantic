from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender:str
    age: int
    address: Address

address_dict={'city':'Mumbai', 'state':'Maharashtra', 'pin':'400001'}

address1=Address(**address_dict)

patient_info={'name':'John Doe','gender':'Male','age':30, 'address':address1}

patient1=Patient(**patient_info)

print(patient1)
print(patient1.address.city)



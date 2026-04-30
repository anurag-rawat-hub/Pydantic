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

temp=patient1.model_dump(include=['name', 'gender', 'age']) #dumps whole model in dict format
temp2=patient1.model_dump_json(exclude=['name', 'gender', 'age'])    #dumps whole model in json format

print(temp)
print(type(temp))
print(temp2)
print(type(temp))




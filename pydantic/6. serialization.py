from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {"city": "gurgoan", "state": "haryana", "pin": "122001"}

address1 = Address(**address_dict)

patient_dict = {"name": "Nitish", "gender": "Male", "age": 35, "address": address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()
print(temp)
print(type(temp))

# Now in the dictionary only name and gender field will be present
temp = patient1.model_dump(include=["name", "gender"])
print(temp)
print(type(temp))

# Now in the dictionary only name and gender field will not be present
temp = patient1.model_dump(exclude=["name", "gender"])
print(temp)
print(type(temp))

# model_dump_json convert into json but python receive in string format and export in the form of json.
temp = patient1.model_dump_json()
print(temp)
print(type(temp))

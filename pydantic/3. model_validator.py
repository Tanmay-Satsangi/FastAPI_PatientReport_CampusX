# If the age is greater than 60, an emergency contact number is required.

from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergy: List[str]
    contact_detail: Dict[str, str]

    @model_validator(mode="after")
    def emergency_contact_number(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_detail:
            raise ValueError("Patient older than 60 must have an emergency contact")
        
        return model


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Updated")

patient_info1 = {"name": "nitish", "email": "abc@hdfc.com", "age": '65', "weight": 75.2, "married": False,"allergy": ["pollen", "dust"], "contact_detail": {"phone": "1234567890", "emergency": "234567"}}

# Unpack the Dictionary
# Pydantic checks that data types match the model definition
patient1 = Patient(**patient_info1)

insert_patient_data(patient1)
update_patient_data(patient1)
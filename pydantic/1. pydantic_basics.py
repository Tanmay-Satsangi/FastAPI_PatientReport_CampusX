from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 characters", examples=["Nitish", "Amit"])]
    email: EmailStr
    # linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=60)
    weight: float = Field(gt=0)
    married: Annotated[bool, Field(default=None, description="Is the patient married or not")]
    allergy: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_detail: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Updated")

patient_info1 = {"name": "nitish", "email": "abc@gmail.com", "linkedin_url": "linkedin.com/", "age": 30, "weight": 75.2, "allergy": ["pollen", "dust"], "contact_detail": {"phone": "1234567890"}}

# Unpack the Dictionary
# Pydantic checks that data types match the model definition
patient1 = Patient(**patient_info1)

insert_patient_data(patient1)
update_patient_data(patient1)
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float

    married: bool
    allergy: List[str]
    contact_detail: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        # If weight = kg and height = meters then use the below formula of bmi
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("BMI: ", patient.calculate_bmi)
    print("Updated")

patient_info1 = {"name": "nitish", "email": "abc@hdfc.com", "age": '65', "weight": 75.2, "height": 1.72, "married": False,"allergy": ["pollen", "dust"], "contact_detail": {"phone": "1234567890", "emergency": "234567"}}

# Unpack the Dictionary
# Pydantic checks that data types match the model definition
patient1 = Patient(**patient_info1)

insert_patient_data(patient1)
update_patient_data(patient1)
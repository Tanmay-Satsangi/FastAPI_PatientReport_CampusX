from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergy: List[str]
    contact_detail: Dict[str, str]

    # @field_validator is a decorator used for custom validation
    # It is defined as a class method
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):  # 'value' represents the email field's value
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
    # @field_validator('name') #field_validator is decorator
    # @classmethod
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    # Before Mode (mode='before')
    @field_validator('age', mode="after")
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Updated")

patient_info1 = {"name": "nitish", "email": "abc@hdfc.com", "age": '30', "weight": 75.2, "married": False,"allergy": ["pollen", "dust"], "contact_detail": {"phone": "1234567890"}}

# Unpack the Dictionary
# Pydantic checks that data types match the model definition
patient1 = Patient(**patient_info1)

insert_patient_data(patient1)
update_patient_data(patient1)
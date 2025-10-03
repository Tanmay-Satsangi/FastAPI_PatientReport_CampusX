from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info1 = {"name": "nitish", "age": 30}

# Unpack the Dictionary
# Pydantic checks that data types match the model definition
patient1 = Patient(**patient_info1)

insert_patient_data(patient1)
update_patient_data(patient1)

# patient_info2 = {"name": "nitish", "age": "thirty"}

# # This line will raise a ValidationError
# # because Pydantic detects that 'age' is not an integer
# patient2 = Patient(**patient_info2)
# # insert_patient_data(**patient2)


from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal # To add the description.
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the patient", example="P001")]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient is living")]
    age: Annotated[int, Field(..., description="Age of the patient")]
    gender: Annotated[Literal["Male", "Female", "Others"], Field(..., description="Gender of the Patient")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient in kgs")]
    weight: Annotated[float, Field(..., gt=0, description="Width of the patient in meters")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"

# Helper function to load and return the data of patient.json file
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
# here patient_id is path parameter which is dynamic in nature
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    
    # return {"error": "patient not found"}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
# Because of ... sort_by is compulsory parameter but order by is optional parameter.
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"), order: str = Query('asc', description="sort in asc or desc order")):
    valid_fields = ["height", "width", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")
    
    data = load_data()

    sort_order = True if order == 'desc' else False

    # reverse:True means sorting in descending order
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

@app.post("/create")
# Patient is a Pydantic model, and 'patient' is the Pydantic object holding the HTTP request data parsed from JSON.

# HTTP Request body data first goes to pydantic model
def create_patient(patient: Patient):
    # 1. load existing data
    data = load_data()

    # 2. check if the patients already exist 
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    # 3. new patient add to the database
    # because data is python dictionary and 'patient' is an pydantic object. So, we have to add 'data' to the pydantic object 'patient'
    # model_dump: Convert pydantic object to dictionary
    data[patient.id] = patient.model_dump(exclude=["id"])

    # 4. Save to the database
    save_data(data)

    return JSONResponse(status_code=201, content={'message': "Patient Created successfully"})

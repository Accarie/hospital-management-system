from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# Patient Schemas
class PatientBase(BaseModel):
    name: str
    age: int
    address: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    appointments: Optional[List["Appointment"]] = []

    class Config:
         from_attributes = True

# Doctor Schemas
class DoctorBase(BaseModel):
    name: str
    specialization: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    appointments: Optional[List["Appointment"]] = []

    class Config:
         from_attributes = True

# Appointment Schemas
class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    date: date
    description: str

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    patient: Optional[Patient]
    doctor: Optional[Doctor]

    class Config:
         from_attributes = True  
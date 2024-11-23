from django import forms
from .models import Doctor, Patient, Appointment, Schedule

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','specialization','contact']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name','age','gender','contact']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment 
        fields = ['patient','doctor','date','time']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['doctor','available_day','start_time','end_time']

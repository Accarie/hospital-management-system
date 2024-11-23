
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Patients URLs
    path('patients/', views.patients, name='patients'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/edit/<int:pk>/', views.patient_edit, name='patient_edit'),
    path('patients/delete/<int:pk>/', views.patient_delete, name='patient_delete'),

    # Doctors URLs
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/create', views.doctor_create, name='doctor_create'),
    path('doctors/edit/<int:pk>/', views.doctor_edit, name='doctor_edit'),
    path('doctors/delete/<int:pk>/', views.doctor_delete, name='doctor_delete'),

    # Appointments URLs
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/edit/<int:pk>/', views.appointment_edit, name='appointment_edit'),
    path('appointments/delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),

    # Schedules URLs
    path('schedules/', views.schedules, name='schedules'),
    path('scheduels/create/', views.schedule_create, name='schedule_create'),
    path('schedules/edit/<int:pk>/', views.schedule_edit, name='schedule_edit'),
    path('schedules/delete/<int:pk>/', views.schedule_delete, name='schedule_delete'),   
    #Analytics URLs

    path('statistics/', views.statistics, name='statistics'),
]



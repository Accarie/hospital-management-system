from django.contrib import admin
from .models import Doctor, Patient, Appointment, Schedule
# Register your models here.(registering your models ensures  they can be managed via django by the admin-interface)

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Schedule)

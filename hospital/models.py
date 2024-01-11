from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    Special = models.CharField(max_length=50)
    yoe = models.IntegerField()
    is_medical_staff = models.BooleanField(default=False) 

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    problem = models.TextField()
    gender = models.CharField(max_length=20)
    address = models.TextField()
    is_patient = models.BooleanField(default=False)
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    




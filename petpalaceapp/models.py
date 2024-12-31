from django.db import models

# Create your models here.
    
from django.db import models
from django.contrib.auth.models import User


class registration(models.Model):
    full_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    pet_info = models.TextField(blank=True)
    address = models.TextField()
    roll = models.CharField(max_length=50, null=True, blank=True)



    

class GroomingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=50, blank=True, null=True)
    grooming_frequency = models.CharField(max_length=50, blank=True, null=True)  # e.g., Weekly, Bi-weekly
    preferred_groomer = models.CharField(max_length=100, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)  # Any allergies related to pets
    special_instructions = models.TextField(blank=True, null=True)  



class BoardingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=50, blank=True, null=True)  # Type of pet (e.g., Dog, Cat)
    boarding_start_date = models.DateField(blank=True, null=True)  # Start date of boarding
    boarding_end_date = models.DateField(blank=True, null=True)  # End date of boarding
    special_needs = models.TextField(blank=True, null=True)  # Any special care or needs






    
    
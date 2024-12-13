from django.db import models

# Create your models here.
    
class petowner_registration(models.Model):
    user=models.TextField(max_length=25,null=True,blank=True)
    address=models.TextField(max_length=25,null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    address=models.TextField(max_length=25,null=True,blank=True)
    password=models.CharField(max_length=25,null=True,blank=True)
    pettype=models.CharField(max_length=25,null=True,blank=True)

    def __str__(self):
        return f'petowner_registration {self.phone}'
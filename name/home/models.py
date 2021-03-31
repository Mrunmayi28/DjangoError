from django.db import models

# Create your models here.
class Plogins(models.Model):
    Name = models.CharField(max_length=30)
    Contact=models.CharField(max_length=40)
    email=models.CharField(max_length=8)
    
  

    


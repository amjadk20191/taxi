from django.db import models

from user.models import User
# Create your models here.

from django.core.validators import  MinValueValidator

class driver(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    description_of_car=models.TextField(default="")
    address=models.TextField()
    active=models.BooleanField(default=False)
    birth_date=models.DateField()
    car_id=models.CharField(max_length=50)
    latitude=models.DecimalField(max_digits=30, decimal_places=15,blank=True, null=True)
    longitude=models.DecimalField(max_digits=30, decimal_places=15,blank=True, null=True)
    
  

   
   


        

class reservation (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(driver, on_delete=models.CASCADE)
    start_latitude=models.CharField(max_length=50)
    start_longitude=models.CharField(max_length=50)
    start_d=models.TextField()
    end_d=models.TextField()
    end_latitude=models.CharField(max_length=50)
    end_longitude=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True,validators=[MinValueValidator(0)])
    date=models.DateField(auto_now_add=True)
 
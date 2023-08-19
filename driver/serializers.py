from rest_framework import serializers
from user.models import User
from driver.models import driver






class driverlocationSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = driver
        fields = ['longitude','latitude']

 
   
        

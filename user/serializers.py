from rest_framework import serializers
from .models import User,problem
from djoser.conf import settings
from driver.models import reservation



class creatproplemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = problem
        fields = ['description']
        
    def create(self, validated_data):   
            validated_data['user']=self.context['request'].user
            return super().create(validated_data)
        
class showreservationSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(source="driver.first_name",read_only=True)
    last_name=serializers.CharField(source="driver.last_name",read_only=True)

    class Meta:
        model = reservation
        fields = ['pk','first_name','last_name','start_d','end_d','price','date']
        


class userCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['password','phone']
        
    def create(self, validated_data):

       
            validated_data['group']='user'
            
            data=super().create(validated_data)
            
            return data

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="key")
    group=serializers.CharField(source="user.group")

    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("auth_token","group",)

from rest_framework import serializers
from user.models import User, problem
from driver.models import driver




class showproplemSerializer(serializers.ModelSerializer):
    phone=serializers.CharField(source='user.phone')
    
    class Meta:
        model = problem
        fields = ['description','phone']


class driverCreateSerializer(serializers.ModelSerializer):
   
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    phone= serializers.CharField(source='user.phone')

    class Meta:
        model = driver
        fields = ['pk','first_name','last_name','gender','description_of_car','address','birth_date','car_id','phone','password']

 
    
    
    def create(self, validated_data):

            user=validated_data.pop('user')
         
            data={
                "group":"driver",
                "phone":user.pop('phone'),
                "password":validated_data.pop('password')
            }
            try:
                validated_data['user']=User.objects.create(**data)
            except:
               raise serializers.ValidationError({"use":"already exist"})    
            
            
            
            
            return super().create(validated_data)
        

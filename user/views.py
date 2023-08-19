from .models import User,problem
from rest_framework import generics,viewsets,views
from .serializers import userCreateSerializer,showreservationSerializer,creatproplemSerializer
from driver.models import driver
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from driver.models import reservation




class showreservation(generics.ListAPIView):

    serializer_class = showreservationSerializer
    
    def get_queryset(self):
        self.queryset = reservation.objects.filter(user=self.request.user)
        return super().get_queryset()



class creatproplem(generics.CreateAPIView):

    queryset = problem.objects.all()
    serializer_class = creatproplemSerializer


class userCreat(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = userCreateSerializer

class  checkcar (views.APIView):


    def post(self, request, *args, **kwargs):
        data=request.data
        distance=abs(abs(data['start_latitude'])-abs(data['end_latitude']))+abs(abs(data['end_longitude'])-abs(data['start_longitude']))
        price=distance*10
        cars=driver.objects.exclude(longitude=None,latitude=None)
        distance_car=[]
        for car in cars:
            distance_car.append(abs(abs(data['start_latitude'])-abs(float(car.latitude)))+abs(abs(float(car.longitude))-abs(data['start_longitude'])))
        min_dis=min(distance_car)
        
        res=model_to_dict(cars[distance_car.index(min_dis)])
        res['price']=price
        
        return Response(res, status=status.HTTP_200_OK)

        
      
class  makereservation (views.APIView):


    def post(self, request, *args, **kwargs):
        data=request.data
        
        
       
        res=model_to_dict(reservation.objects.create(driver=driver(pk=data['pk']),start_latitude=data['start_latitude'],start_longitude=data['start_longitude'],end_latitude=data['end_latitude'],end_longitude=data['end_longitude'],price=data['price'],user=request.user))
        driver.objects.filter(pk=data['pk']).update(active=True)
        
        return Response(res, status=status.HTTP_200_OK)

        
      

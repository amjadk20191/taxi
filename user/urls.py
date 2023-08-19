from django.urls import path,include
from rest_framework import routers
from .views import userCreat,checkcar,makereservation,showreservation,creatproplem
router = routers.DefaultRouter()

urlpatterns = [
    path('', userCreat.as_view(), name="user-Creat"),
    path('checkcar/', checkcar.as_view(), name="checkcar"),
    path('reservation/', makereservation.as_view(), name="reservation"),
    path('showreservation/', showreservation.as_view(), name="showreservation"),
    path('proplem/', creatproplem.as_view(), name="creatproplem"),
    
    
    path('', include(router.urls)),

]
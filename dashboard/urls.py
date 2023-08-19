from django.urls import path,include
from rest_framework import routers
from .views import driverCreat ,showproblem
router = routers.DefaultRouter()
router.register(r'driver', driverCreat, basename="driver")

urlpatterns = [
    # path('', advertiserCreat.as_view(), name="advertiser-creat"),
    
        path('showproblem/', showproblem.as_view(), name="showproblem"),

    path('', include(router.urls)),

]
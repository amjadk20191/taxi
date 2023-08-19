from django.urls import path,include
from rest_framework import routers
from .views import driverlocation
router = routers.DefaultRouter()

urlpatterns = [
    path('location-update/', driverlocation.as_view(), name="location-update"),
    
    
    path('', include(router.urls)),

]
from driver.models import driver
from rest_framework import generics,viewsets,views
from .serializers import driverlocationSerializer


    
class driverlocation(generics.UpdateAPIView):
    http_method_names=['patch',]

    serializer_class = driverlocationSerializer
    def get_object(self):

        return driver.objects.get(pk=self.request.user.driver.pk)



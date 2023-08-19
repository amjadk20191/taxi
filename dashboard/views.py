from driver.models import driver
from rest_framework import generics,viewsets,views
from .serializers import driverCreateSerializer,showproplemSerializer
from rest_framework import status
from rest_framework.response import Response
from user.models import User ,problem

class showproblem (generics.ListAPIView):
    serializer_class=showproplemSerializer
    queryset=problem.objects.all()

class driverCreat(viewsets.ModelViewSet):

    queryset = driver.objects.all()
    serializer_class = driverCreateSerializer
    def destroy(self, request, *args, **kwargs):
        instance = User.objects.get(pk=self.request.user.driver.pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
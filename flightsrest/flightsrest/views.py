from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from flightsrest.flightsrest.serializers import UserSerializer, GroupSerializer, AircraftSerializer, AirportSerializer
from flightsrest.flightsrest.models import Aircraft, Airport
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AircraftViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows aircrafts to be viewed
    """    
    queryset = Aircraft.objects.all().order_by('-range')
    serializer_class = AircraftSerializer

class AirportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows airports to be viewed
    """
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
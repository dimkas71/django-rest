from django.contrib.auth.models import User, Group
from flightsrest.flightsrest.models import Aircraft, Airport
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AircraftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft
        fields = ('aircraft_code', 'model', 'range')

class AirportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airport
        fields = ('airport_code', 'airport_name', 'city', 'timezone')

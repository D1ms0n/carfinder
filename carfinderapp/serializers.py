import time

from rest_framework import serializers
from django.contrib.auth.models import User

from carfinderapp.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
                  'username',
                  'email'
                  )

class _CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('pk',
                  'manufacturer',
                  'model',
                  'color',
                  'year',
                  'mileage',
                  )


class SnoopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snoop
        fields = ('pk',
                  'model',
                  'manufacturer',
                  'year_min',
                  'year_max',
                  'mileage_min',
                  'mileage_max',
                  )

class SnoopSerializerWithCars(serializers.ModelSerializer):
    cars = _CarSerializer(many=True)

    class Meta:
        model = Snoop
        fields = ('pk',
                  'manufacturer',
                  'model',
                  'year_min',
                  'year_max',
                  'mileage_min',
                  'mileage_max',
                  'cars'
                  )


class _SnoopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snoop
        fields = ('pk',)


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('pk',
                  'manufacturer',
                  'model',
                  'color',
                  'year',
                  'mileage',
                  )


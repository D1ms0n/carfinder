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

class _ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = (
                  'manufacturer_name',
                  )

class _ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = (
                  'model_name',
                  )

class CarSerializer(serializers.ModelSerializer):
    # manufacturer_id =_ManufacturerNameSerializer()
    # model_id = _ModelNameSerializer()
    class Meta:
        model = Car
        fields = ('pk',
                  'manufacturer_id',
                  'model_id',
                  'color',
                  'year',
                  'mileage',
                  )

class SnoopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnoopDetail

        fields = ('manufacturer',
                  'model',
                  'year_min',
                  'year_max',
                  'mileage_min',
                  'mileage_max',
                  )

class SnoopSerializer(serializers.ModelSerializer):
    details =SnoopDetailSerializer(many=True)

    class Meta:
        model = Snoop

        fields = ('id',
                  'user',
                  'details',
                  )

    def create(self, validated_data):
        detail_data = validated_data.pop('details')

        snoop = Snoop.objects.create(**validated_data)

        for detail in detail_data:
            SnoopDetail.objects.create(**detail, snoop = snoop)

        return snoop

class SnoopSerializerWithCars(serializers.ModelSerializer):
    cars = CarSerializer(many=True)

    class Meta:
        model = Snoop
        fields = ('relations',)


class _SnoopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snoop
        fields = ('pk',)

#
# class CarSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Car
#         fields = ('pk',
#                   'manufacturer',
#                   'model',
#                   'color',
#                   'year',
#                   'mileage',
#                   )


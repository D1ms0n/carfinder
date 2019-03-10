from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import generics
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from carfinderapp.serializers import *
from carfinderapp.models import *

# TODO PUT /api/snoops/1/
# TODO PUT /api/snoops/1/details/1

# TODO DEL /api/snoops/1/
# TODO DEL /api/snoops/1/details/1

class SnoopList(generics.ListCreateAPIView):       # TODO check if model is related to manufacturer
    serializer_class = SnoopSerializer
    renderer_classes = (JSONRenderer,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Snoop.objects.all().filter(user=self.request.user)

class SnoopDetail(generics.RetrieveAPIView):
    queryset = Snoop.objects.all()
    serializer_class = SnoopSerializer
    renderer_classes = (JSONRenderer,)
    lookup_field = 'pk'

class SnoopCars(generics.ListAPIView):
    serializer_class = CarSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        cars = Car.objects.filter(relations__snoop__id = self.kwargs['pk'])

        return cars
class CarDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    renderer_classes = (JSONRenderer,)
    lookup_field = 'pk'

# class CarList(generics.ListAPIView):              # TODO filter by user.  USER -> SNOOPS -> CARS
#     serializer_class = CarSerializer
#     renderer_classes = (JSONRenderer,)
#
#     def get_queryset(self):
#         return Car.objects.all()


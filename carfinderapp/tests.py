# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from carfinderapp.models import *


# TESTS:
# GET /api/snoops/
# POST /api/snoops/
# TODO /api/snoops/1/
# GET /api/snoops/1/cars/
# TODO /api/cars/1/

# TODO PUT /api/snoops/1/
# TODO PUT /api/snoops/1/details/1

# TODO DEL /api/snoops/1/
# TODO DEL /api/snoops/1/details/1




user_name_1 = "test_user1"
user_name_2 = "test_user2"

user_password_1 = 'test_password1'
user_password_2 = 'test_password2'

user_email_1 = "test1@tst.com"
user_email_2 = "test2@tst.com"

manufacturer_name_1 = "manufacturer_name_1"
manufacturer_name_2 = "manufacturer_name_2"

model_name_1_1 = "model_name_1_1"
model_name_1_2 = "model_name_1_2"
model_name_2_1 = "model_name_2_1"
model_name_2_2 = "model_name_2_2"


car_url1 = "https://blabla.bla/car1"
car_url2 = "https://blabla.bla/car2"
car_url3 = "https://blabla.bla/car3"
car_url4 = "https://blabla.bla/car4"


class APITests(APITestCase):
    def setUp(self):

        # Create users, manufacturers and
        self.user_1 = User.objects.create_user(user_name_1, user_email_1, user_password_1)
        self.user_2 = User.objects.create_user(user_name_2, user_email_2, user_password_2)

        self.manufacturer_1 = Manufacturer.objects.create(manufacturer_name = manufacturer_name_1)
        self.manufacturer_2 = Manufacturer.objects.create(manufacturer_name = manufacturer_name_2)

        self.model_1_1 = Model.objects.create(model_name=model_name_1_1, manufacturer=self.manufacturer_1)
        self.model_1_2 = Model.objects.create(model_name=model_name_1_2, manufacturer=self.manufacturer_1)
        self.model_2_1 = Model.objects.create(model_name=model_name_2_1, manufacturer=self.manufacturer_2)
        self.model_2_2 = Model.objects.create(model_name=model_name_2_2, manufacturer=self.manufacturer_2)


    def test_api_snoops_get_1(self):
        # Test get of single snoop with two details
        url = "/api/snoops/"

        expected_data = [OrderedDict([('id', 1), ('user', 1), ('details', [OrderedDict([('manufacturer', 'manufacturer_name_1'),
                                                                                        ('model', 'model_name_1_1')]),
                                                                           OrderedDict([('manufacturer', 'manufacturer_name_2'),
                                                                                        ('model', 'model_name_2_1')])])]),
                         OrderedDict([('id', 2), ('user', 1), ('details', [OrderedDict([('manufacturer', 'manufacturer_name_1'),
                                                                                        ('model', 'model_name_1_1')]),
                                                                           OrderedDict([('manufacturer', 'manufacturer_name_2'),
                                                                                        ('model', 'model_name_2_1')])])])]

        # Create test snoops with details for user_1
        # User 1, Snoop 1
        snoop_1_1 = Snoop.objects.create(user = self.user_1)
        # User 1, Snoop 2
        snoop_1_2 = Snoop.objects.create(user = self.user_1)

        detail_1_1 =  SnoopDetail.objects.create(snoop = snoop_1_1, manufacturer = self.manufacturer_1, model = self.model_1_1)
        detail_1_1 =  SnoopDetail.objects.create(snoop = snoop_1_1, manufacturer = self.manufacturer_2, model = self.model_2_1)
        detail_2_1 =  SnoopDetail.objects.create(snoop = snoop_1_2, manufacturer = self.manufacturer_1, model = self.model_1_1)
        detail_2_2 =  SnoopDetail.objects.create(snoop = snoop_1_2, manufacturer = self.manufacturer_2, model = self.model_2_1)

        # Create test snoops with details for user_2
        # User 2, Snoop 1
        snoop_1_1 = Snoop.objects.create(user=self.user_2)
        # User 2, Snoop 2
        snoop_1_2 = Snoop.objects.create(user=self.user_2)

        detail_1_1 = SnoopDetail.objects.create(snoop=snoop_1_1, manufacturer=self.manufacturer_1, model=self.model_1_1)
        detail_1_1 = SnoopDetail.objects.create(snoop=snoop_1_1, manufacturer=self.manufacturer_2, model=self.model_2_1)
        detail_2_1 = SnoopDetail.objects.create(snoop=snoop_1_2, manufacturer=self.manufacturer_1, model=self.model_1_1)
        detail_2_2 = SnoopDetail.objects.create(snoop=snoop_1_2, manufacturer=self.manufacturer_2, model=self.model_2_1)

        self.client.login(username='test_user1', password='test_password1')

        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        self.assertEqual(get_response.data, expected_data)

    def test_api_snoops_create_1(self):
        # Test creating of single snoop with two details
        url = "/api/snoops/"

        data = {"details": [{"manufacturer": manufacturer_name_1, "model": model_name_1_1},
                            {"manufacturer": manufacturer_name_2, "model": model_name_2_1}]}

        expected_data = [OrderedDict([('id', 1), ('user', 1), ('details', [
                         OrderedDict([('manufacturer', 'manufacturer_name_1'), ('model', 'model_name_1_1')]),
                         OrderedDict([('manufacturer', 'manufacturer_name_2'), ('model', 'model_name_2_1')])])])]

        self.client.login(username='test_user1', password='test_password1')

        post_response = self.client.post(url, data, format='json')
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)


        get_response = self.client.get("/api/snoops/")
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        self.assertEqual(get_response.data, expected_data)

    def test_get_snoop_cars(self):
        url = "/api/snoops/1/cars/"

        expected_data = [OrderedDict([('pk', 1),
                                      ('manufacturer_id', 'manufacturer_name_1'),
                                      ('model_id', 'model_name_1_1'),
                                      ('color', 'red'),
                                      ('year', 1991),
                                      ('mileage', 1000)]),
                         OrderedDict([('pk', 2),
                                      ('manufacturer_id', 'manufacturer_name_2'),
                                      ('model_id', 'model_name_2_1'),
                                      ('color', 'black'),
                                      ('year', 1981),
                                      ('mileage', 1400)])]

        # Create a snoop
        snoop_1_1 = Snoop.objects.create(user=self.user_1)
        snoop_2_1 = Snoop.objects.create(user=self.user_2)


        # Create cars related to the snoop
        car_1 = Car.objects.create(url = car_url1,
                                   color = "red",
                                   mileage = 1000,
                                   year = 1991,
                                   manufacturer = self.manufacturer_1,
                                   model = self.model_1_1)

        car_2 = Car.objects.create(url=car_url2,
                                   color="black",
                                   mileage=1400,
                                   year=1981,
                                   manufacturer=self.manufacturer_2,
                                   model=self.model_2_1)

        # Create car to snoop relations

        rel1 = CarToSnoopRelation.objects.create(car = car_1, snoop = snoop_1_1)
        rel2 = CarToSnoopRelation.objects.create(car = car_2, snoop = snoop_1_1)

        # Create cars related to the snoop
        car_3 = Car.objects.create(url=car_url3,
                                   color="red",
                                   mileage=1000,
                                   year=1991,
                                   manufacturer=self.manufacturer_1,
                                   model=self.model_1_1)

        car_4 = Car.objects.create(url=car_url4,
                                   color="black",
                                   mileage=1400,
                                   year=1981,
                                   manufacturer=self.manufacturer_2,
                                   model=self.model_2_1)

        # Create car to snoop relations

        rel1 = CarToSnoopRelation.objects.create(car=car_3, snoop=snoop_2_1)
        rel2 = CarToSnoopRelation.objects.create(car=car_4, snoop=snoop_2_1)

        self.client.login(username='test_user1', password='test_password1')

        get_response = self.client.get(url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        self.assertEqual(get_response.data, expected_data)
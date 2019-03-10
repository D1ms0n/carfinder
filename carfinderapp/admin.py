# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.sessions.models import Session


from .models import *

# Register your models here.



# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(ManufacturerId)
admin.site.register(Model)
admin.site.register(ModelId)
admin.site.register(Snoop)
admin.site.register(SnoopDetail)
admin.site.register(Car)
admin.site.register(CarToSnoopRelation)
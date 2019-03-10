# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    class Meta(object):
        verbose_name = u"Manufacturer Name"
        verbose_name_plural = u"Manufacturer Names"
    def __unicode__(self):
        return u"%s..." % (self.manufacturer_name)

    manufacturer_name = models.CharField(max_length=256, primary_key=True, blank=False, verbose_name=u"Manufacturer Name")   # BMW

class ManufacturerId(models.Model):   # internal
    class Meta(object):
        verbose_name = u"Manufacturer Id"
        verbose_name_plural = u"Manufacturer Ids"
    def __unicode__(self):
        return u"%s..." % (self.name)

    # manufacturer_id = models.CharField(max_length=256, blank=False, verbose_name=u"Manufacturer", null= True)
    name = models.ForeignKey(Manufacturer, blank=True, null=True, related_name='manufacturer_ids', on_delete=models.CASCADE)

    autoria_id = models.CharField(max_length=256, blank=False, verbose_name=u"Autoria_Id", null= True)
    rst_id = models.CharField(max_length=256, blank=False, verbose_name=u"RST_Id", null= True)

class Model(models.Model):

    class Meta(object):
        verbose_name = u"Model Name"
        verbose_name_plural = u"Model Names"

    def __unicode__(self):
        return u"%s..." % (self.model_name)


    model_name = models.CharField(primary_key=True, max_length=256,  verbose_name=u"Model Name")
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, related_name='model_names', on_delete=models.CASCADE)

class ModelId(models.Model):
    class Meta(object):
        verbose_name = u"Model Id"
        verbose_name_plural = u"Model Ids"
    def __unicode__(self):
        return u"%s..." % (self.model_name)

    model_name = models.ForeignKey(Model, blank=True, null=True, related_name='model_ids', on_delete=models.CASCADE)
    autoria_id = models.CharField(max_length=256, blank=False, verbose_name=u"Autoria_Id", null= True)
    rst_id = models.CharField(max_length=256, blank=False, verbose_name=u"RST_Id", null= True)
    # manufacturer = models.ForeignKey(ManufacturerName, blank=True, null=True, related_name='models', on_delete=models.CASCADE)


class Snoop(models.Model):
    class Meta(object):
        verbose_name = u"Snoop"
        verbose_name_plural = u"Snoops"
    def __unicode__(self):
        return u"%s..." % ("snoop")

    user         = models.ForeignKey(User, blank = True, null= True, related_name='snoops', on_delete=models.CASCADE)

class SnoopDetail(models.Model):
    class Meta(object):
        verbose_name = u"SnoopDetail"
        verbose_name_plural = u"SnoopDetails"
    def __unicode__(self):
        return u"%s..." % (self.model)

    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, related_name='snoops',
                                     on_delete=models.CASCADE)

    model = models.ForeignKey(Model, blank=True, null=True, related_name='snoops',
                              on_delete=models.CASCADE)

    year_min = models.IntegerField(blank=True, null=True, verbose_name=u"Year min")
    year_max = models.IntegerField(blank=True, null=True, verbose_name=u"Year max")
    mileage_min = models.IntegerField(blank=True, null=True, verbose_name=u"Mileage min")
    mileage_max = models.IntegerField(blank=True, null=True, verbose_name=u"Mileage max")

    snoop = models.ForeignKey(Snoop, blank=True, null=True, related_name='details', on_delete=models.CASCADE)

class Car(models.Model):
    class Meta(object):
        verbose_name = u"Car"
        verbose_name_plural = u"Cars"
    def __unicode__(self):
        return u"%s..." % (self.id)


    url          = models.CharField(max_length=256, blank=False, verbose_name=u"URL", null= True)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, related_name='cars',
                                     on_delete=models.CASCADE)

    model = models.ForeignKey(Model, blank=True, null=True, related_name='cars',
                              on_delete=models.CASCADE)
    color        = models.CharField(max_length=256, blank=True, verbose_name=u"Color", null= True)
    year         = models.IntegerField(blank=True,verbose_name=u"Year")
    mileage      = models.IntegerField(blank=True,verbose_name=u"Mileage")

class CarToSnoopRelation(models.Model):
    class Meta(object):
        verbose_name = u"Car to Snoop relation"
        verbose_name_plural = u"Car to Snoop relations"
    def __unicode__(self):
        return u"%s..." % ("car")

    car   = models.ForeignKey(Car, blank=True, null=True, related_name='relations', on_delete=models.CASCADE)
    snoop = models.ForeignKey(Snoop, blank=True, null=True, related_name='relations', on_delete=models.CASCADE)  # CHECK!


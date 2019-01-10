# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class ManufacturerId(models.Model):
    class Meta(object):
        verbose_name = u"Manufacturer Id"
        verbose_name_plural = u"Manufacturer Ids"
    def __unicode__(self):
        return u"%s..." % (self.id)

    manufacturer = models.CharField(max_length=256, blank=False, verbose_name=u"Manufacturer", null= True)
    autoria_id = models.CharField(max_length=256, blank=False, verbose_name=u"Autoria_Id", null= True)
    rst_id = models.CharField(max_length=256, blank=False, verbose_name=u"Autoria_Id", null= True)

class ModelId(models.Model):
    class Meta(object):
        verbose_name = u"Model Id"
        verbose_name_plural = u"Model Ids"
    def __unicode__(self):
        return u"%s..." % (self.id)

    model = models.CharField(max_length=256, blank=False, verbose_name=u"Model", null= True)
    autoria_id = models.CharField(max_length=256, blank=False, verbose_name=u"Autoria_Id", null= True)
    rst_id = models.CharField(max_length=256, blank=False, verbose_name=u"Autoria_Id", null= True)
    manufacturer = models.ForeignKey(ManufacturerId, blank=True, null=True, related_name='models', on_delete=models.CASCADE)


class Snoop(models.Model):
    class Meta(object):
        verbose_name = u"Snoop"
        verbose_name_plural = u"Snoops"
    def __unicode__(self):
        return u"%s..." % (self.model)

    #id           = models.Pr(primary_key = True)
    model        = models.CharField(max_length=256, blank=False, verbose_name=u"Model", null=True)
    manufacturer = models.CharField(max_length=256, blank=False, verbose_name=u"Manufacturer", null= True)

    year_min     = models.IntegerField(blank=True,null=True, verbose_name=u"Year min")
    year_max     = models.IntegerField(blank=True,null=True, verbose_name=u"Year max")
    mileage_min  = models.IntegerField(blank=True, null=True, verbose_name=u"Mileage min")
    mileage_max  = models.IntegerField(blank=True, null=True, verbose_name=u"Mileage max")

    user         = models.ForeignKey(User, blank = True, null= True, related_name='snoops', on_delete=models.CASCADE)



class Car(models.Model):
    class Meta(object):
        verbose_name = u"Car"
        verbose_name_plural = u"Cars"
    def __unicode__(self):
        return u"%s..." % (self.model)

    #id           = models.AutoField(primary_key=True)
    url          = models.CharField(max_length=256, blank=False, verbose_name=u"URL", null= True)
    manufacturer = models.CharField(max_length=256, blank=False, verbose_name=u"Manufacturer", null= True)
    model        = models.CharField(max_length=256, blank=False, verbose_name=u"Model", null=True)
    color        = models.CharField(max_length=256, blank=True, verbose_name=u"Color", null= True)

    year         = models.IntegerField(blank=True,verbose_name=u"Year")
    mileage      = models.IntegerField(blank=True,verbose_name=u"Mileage")

   # snoop        = models.ForeignKey(Snoop, related_name='cars', on_delete=models.CASCADE)


class CarToSnoopRelation(models.Model):
    class Meta(object):
        verbose_name = u"Car to Snoop relation"
        verbose_name_plural = u"Car to Snoop relations"
    def __unicode__(self):
        return u"%s..." % (self.id)

    car   = models.ForeignKey(Car, blank=True, null=True, related_name='relations', on_delete=models.CASCADE)
    snoop = models.ForeignKey(Snoop, blank=True, null=True, related_name='relations', on_delete=models.CASCADE)  # CHECK!


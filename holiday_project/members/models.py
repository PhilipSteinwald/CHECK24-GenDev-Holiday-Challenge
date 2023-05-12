from django.db import models

class Offers(models.Model):
    hotelid = models.DecimalField(max_digits=32, decimal_places=0)
    outbounddeparturedatetime = models.DateTimeField()
    inbounddeparturedatetime = models.DateTimeField()
    countadults = models.DecimalField(max_digits=3, decimal_places=0)
    countchildren = models.DecimalField(max_digits=3, decimal_places=0)
    price = models.DecimalField(max_digits=32, decimal_places=0)
    inbounddepartureairport = models.CharField(max_length=3)
    inboundarrivalairport = models.CharField(max_length=3)
    inboundarrivaldatetime = models.DateTimeField()
    outbounddepartureairport = models.CharField(max_length=3)
    outboundarrivalairport = models.CharField(max_length=3)
    outboundarrivaldatetime = models.DateTimeField()
    mealtype = models.CharField(max_length=32)
    oceanview = models.BooleanField()
    roomtype = models.CharField(max_length=32)
    startdate = models.DateField()
    enddate = models.DateField()
    days = models.DecimalField(max_digits=3, decimal_places=0)

class Hotel(models.Model):
    hotelid = models.DecimalField(max_digits=32, decimal_places=0, primary_key=True)
    hotelname = models.CharField(max_length=32)
    hotelstars = models.DecimalField(max_digits=2, decimal_places=1)
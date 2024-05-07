from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Laundry(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, blank=True)
    topwearqty = models.CharField(max_length=100, null=True, blank=True)
    bottomwearqty = models.CharField(max_length=100, null=True, blank=True)
    woolenclothqty = models.CharField(max_length=100, null=True, blank=True)
    other = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, default="New", null=True, blank=True)
    servicetype = models.CharField(max_length=100, null=True, blank=True)
    contactperson = models.CharField(max_length=100, null=True, blank=True)
    pickupaddress = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    todate = models.DateField(null=True, blank=True)
    fromdate = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    other_price = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

class About(models.Model):
   pagetitle = models.CharField(max_length=100, null=True, blank=True)
   description = models.CharField(max_length=100, null=True, blank=True)

class Price(models.Model):
    bottomwearprice = models.CharField(max_length=100, null=True, blank=True)
    topwearprice = models.CharField(max_length=100, null=True, blank=True)
    woolenprice = models.CharField(max_length=100, null=True, blank=True)
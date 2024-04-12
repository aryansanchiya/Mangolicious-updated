from django.db import models
from django.db.models import Model
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus
# Create your models here.


class BuyNow(models.Model):
    Ahmedabad = models.IntegerField()
    Rajkot = models.IntegerField()
    Mumbai = models.IntegerField()
    Jamnagar = models.IntegerField()
    Khambhaliya = models.IntegerField()
    Surat = models.IntegerField()
    Baroda = models.IntegerField()
    Junagadh = models.IntegerField()
    SavarKundla = models.IntegerField()
    Viramgam = models.IntegerField()
    Wankaner = models.IntegerField()
    Amreli = models.IntegerField()
    Gondal = models.IntegerField()
    Jetpur = models.IntegerField()
    Porbandar = models.IntegerField()
    Bhavnagar = models.IntegerField()
    Veraval = models.IntegerField()
    Talala_Gir = models.IntegerField()
    Una = models.IntegerField()
    Kodinar = models.IntegerField()
    Dwarka = models.IntegerField()
    quantity = models.IntegerField()
    quantityIn = models.CharField(max_length = 200)

class RipeMangoes(models.Model):
    Ahmedabad = models.IntegerField()
    Rajkot = models.IntegerField()
    Mumbai = models.IntegerField()
    Jamnagar = models.IntegerField()
    Khambhaliya = models.IntegerField()
    Surat = models.IntegerField()
    Baroda = models.IntegerField()
    Junagadh = models.IntegerField()
    SavarKundla = models.IntegerField()
    Viramgam = models.IntegerField()
    Wankaner = models.IntegerField()
    Amreli = models.IntegerField()
    Gondal = models.IntegerField()
    Jetpur = models.IntegerField()
    Porbandar = models.IntegerField()
    Bhavnagar = models.IntegerField()
    Veraval = models.IntegerField()
    Talala_Gir = models.IntegerField()
    Una = models.IntegerField()
    Kodinar = models.IntegerField()
    Dwarka = models.IntegerField()
    quantity = models.IntegerField()
    quantityIn = models.CharField(max_length = 200)

class Details(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    Mo_No = models.IntegerField()
    quant = models.IntegerField()
    city = models.CharField(max_length=200)
    typeofmangoes = models.CharField(max_length=255)
    Choice = models.CharField(max_length=200)
    address = models.TextField()
    total_price = models.FloatField(null=True)
    payment_id = models.CharField(max_length=255,null=True)
    # created_at = models.DateTimeField(auto_now_add=False)

class Cod(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    Mo_No = models.IntegerField()
    quant = models.IntegerField()
    city = models.CharField(max_length=200)
    typeofmangoes = models.CharField(max_length=255)
    Choice = models.CharField(max_length=200)
    address = models.TextField()



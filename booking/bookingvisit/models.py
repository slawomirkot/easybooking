from django.db import models
from djangoratings import RatingField
from phone_field import PhoneField


class HServices(models.Model):
    service = models.CharField(max_length=128)
    time_service = models.IntegerField()
    price_service = models.IntegerField()

class Hairdresser(models.Model):
    name = models.TextField()
    surname = models.TextField()
    services = models.ManyToManyField(HServices)
    workplace_number = models.IntegerField()

class BServices(models.Model):
    service = models.CharField(max_length=128)
    time_service = models.IntegerField()
    price_service = models.IntegerField()

class Beautician(models.Model):
    name = models.TextField()
    surname = models.TextField()
    services = models.ManyToManyField(BServices)
    workplace_number = models.IntegerField()

class Client_Profil(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True, blank=False)
    phone_number = PhoneField(unique=True, blank=False)
    last_login = models.DateField(auto_now=True)
    date_joined = models.DateField(auto_now_add=True)

class Employees(models.Model):
    hairdresser = models.ManyToManyField(Hairdresser)
    beautician = models.ManyToManyField(Beautician)

class Reservation(models.Model):
    client = models.ForeignKey(Client_Profil, on_delete=models.CASCADE, primary_key=True)
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE, primary_key=True)
    services = models.ManyToManyField(BServices, HServices)

class Opinions(models.Model):
    rating = RatingField(range=5)
    name = models.ForeignKey(Client_Profil, on_delete=models.CASCADE, primary_key=True)
    opinion = models.TextField()
    data = models.DateField(auto_now=True)
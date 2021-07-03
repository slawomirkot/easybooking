import datetime
from django.db import models
from django.contrib.auth.models import User



class HServices(models.Model):
    service = models.CharField(max_length=128)
    time_service = models.IntegerField()
    price_service = models.IntegerField()

    def __str__(self):
        return self.service

    class Meta:
        verbose_name_plural = '3 Usługi fryzjerskie'

class Hairdresser(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    services = models.ManyToManyField(HServices)
    workplace_number = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name_plural = '1 Fryzjerzy'
        verbose_name = 'Fryzjera'

class BServices(models.Model):
    service = models.CharField(max_length=128)
    time_service = models.IntegerField()
    price_service = models.IntegerField()

    def __str__(self):
        return self.service

    class Meta:
        verbose_name_plural = '4 Usługi kosmetyczne'

class Beautician(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=64)
    services = models.ManyToManyField(BServices)
    workplace_number = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name_plural = '2 Kosmetyczki'

class Client_Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=12, default='brak numeru')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.email} {self.phone_number}'

    class Meta:
        def __str__(self):
            return f'{self.user.username} Profil'
        verbose_name_plural = '5 Użytkownicy'


class Reservation_Hairdresser(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    employees = models.ForeignKey(Hairdresser, on_delete=models.CASCADE, verbose_name='Pracownik')
    services = models.ForeignKey(HServices, on_delete=models.CASCADE, verbose_name='Usługa')
    day = models.DateField(default=datetime.date.today, verbose_name='Data')
    start_time = models.TimeField(default='08:00', verbose_name='Godzina')

    def __str__(self):
        return f'{self.day} {self.start_time}'

    class Meta:
        verbose_name_plural = '6 Rezerwacje do fryzjera'

class Reservation_Beautician(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    employees = models.ForeignKey(Beautician, on_delete=models.CASCADE, verbose_name='Pracownik')
    services = models.ForeignKey(BServices, on_delete=models.CASCADE, verbose_name='Usługa')
    day = models.DateField(default=datetime.date.today, verbose_name='Data')
    start_time = models.TimeField(default='09:00', verbose_name='Godzina')

    def __str__(self):
        return f'{self.day} {self.start_time}'

    class Meta:
        verbose_name_plural = '7 Rezerwacje do kosmetyczki'

class Opinions(models.Model):
    objects = None
    rating = models.IntegerField(default=round(5))
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    opinion = models.TextField()
    data = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.data}'

    class Meta:
        verbose_name_plural = '8 Opinie'
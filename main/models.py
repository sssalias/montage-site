from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    name = models.TextField()
    price = models.FloatField()
    radius = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.price} руб. {self.radius} - радиус'


class AddotionalServices(models.Model):
    name = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.name} {self.price} руб.'


class ServicesTypes(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'
    

class Services(models.Model):
    type_id = models.ForeignKey(ServicesTypes, on_delete=models.CASCADE)
    name = models.TextField()
    radius = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.radius} - радиус {self.type_id} id типа'


class Appointments(models.Model):
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    type_id = models.ForeignKey(ServicesTypes, on_delete=models.CASCADE)
    service = models.TextField()
    serivce_type = models.TextField()
    bio = models.TextField()
    radius = models.IntegerField()
    phone = models.TextField()
    date = models.DateField()
    time = models.TimeField()

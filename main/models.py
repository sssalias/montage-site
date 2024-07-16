import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class ProductsType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'

# class Products(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.TextField()
#     price = models.FloatField()
#     radius = models.IntegerField()
#     type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.name} {self.price} руб. {self.radius} - радиус'



class ServicesTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'
    

class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_id = models.ForeignKey(ServicesTypes, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f'{self.name} {self.type_id} типа услуги'

class ServicesRadius(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()


class Appointments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    type_id = models.ForeignKey(ServicesTypes, on_delete=models.CASCADE)
    service = models.TextField()
    serivce_type = models.TextField()
    bio = models.TextField()
    radius = models.IntegerField()
    phone = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    


class Storage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'
    

class LightService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'


class HardService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'    
    

class FullLightService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'
    

class FullHardService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'


class AddotionalServices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name} {self.price} руб.'

import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class ProductsType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()

    class Meta:
        verbose_name = 'Тип продукта/услуги'
        verbose_name_plural = 'Тип продукта/услуги'

    def __str__(self):
        return f'{self.name}'


class ServicesTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()

    class Meta:
        verbose_name = 'Услуги (для формы)'
        verbose_name_plural = 'Услуги (для формы)'

    def __str__(self):
        return f'{self.name}'
    

class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_id = models.ForeignKey(ServicesTypes, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name = 'Тип услуги (для формы)'
        verbose_name_plural = 'Тип услуги (для формы)'

    def __str__(self):
        return f'{self.name} {self.type_id} типа услуги'

class ServicesRadius(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()

    class Meta:
        verbose_name = 'Радиус (для таблицы)'
        verbose_name_plural = 'Радиус (для таблицы)'

    def __str__(self):
        return f'{self.radius}'


class ServiceTime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.TimeField()

    class Meta:
        verbose_name = 'Время (для формы)'
        verbose_name_plural = 'Время (для формы)'

    def __str__(self):
        return f'{self.time}'


class Appointments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    type = models.ForeignKey(ServicesTypes, on_delete=models.CASCADE)
    bio = models.TextField()
    radius = models.IntegerField()
    phone = models.TextField()
    date = models.DateField()
    time = models.ForeignKey(ServiceTime, on_delete=models.CASCADE) 
    message = models.TextField(null=True)

    class Meta:
        verbose_name = 'Записи (форма)'
        verbose_name_plural = 'Записи (форма)'

    def __str__(self):
        return f'{self.type} {self.service} {self.radius} {self.date} {self.time}'


class Storage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Хранение шин (для таблицы)'
        verbose_name_plural = 'Хранение шин  (для таблицы)'

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'
    

class LightService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Шиномонтаж легковых автомобилей (для таблицы)'
        verbose_name_plural = 'Шиномонтаж легковых автомобилей (для таблицы)'

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'


class HardService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Шиномонтаж внедорожники, кроссоверы и минивэны (для таблицы)'
        verbose_name_plural = 'Шиномонтаж внедорожники, кроссоверы и минивэны  (для таблицы)'

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'    
    

class FullLightService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фулл прайс шиномонтажа легковых автомобилей (для таблицы)'
        verbose_name_plural = 'Фулл прайс шиномонтаж легковых автомобилей (для таблицы)'

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'
    

class FullHardService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radius = models.IntegerField()
    price = models.FloatField(default=0)
    type = models.ForeignKey(ProductsType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фулл прайс шиномонтаж внедорожники, кроссоверы и минивэны (для таблицы)'
        verbose_name_plural = 'Фулл прайс шиномонтаж внедорожники, кроссоверы и минивэны  (для таблицы)'

    def __str__(self):
        return f'{self.type}, радиус - {self.radius}'


class AddotionalServices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    price = models.FloatField(default=0)

    class Meta:
            verbose_name = 'Доплаты и дополнительные работы (за одно колесо) (для таблицы)'
            verbose_name_plural = 'Доплаты и дополнительные работы (за одно колесо) (для таблицы)'


    def __str__(self):
        return f'{self.name} {self.price} руб.'

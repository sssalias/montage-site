from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(ProductsType)
class ProductsTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    ...


@admin.register(LightService)
class LightServiceAdmin(admin.ModelAdmin):
    ...


@admin.register(HardService)
class HardServiceAdmin(admin.ModelAdmin):
    ...


@admin.register(FullLightService)
class FullLightServiceAdmin(admin.ModelAdmin):
    ...


@admin.register(FullHardService)
class FullHardServiceAdmin(admin.ModelAdmin):
    ...


@admin.register(AddotionalServices)
class AddotionalServicesAdmin(admin.ModelAdmin):
    ...

@admin.register(ServicesTypes)
class ServiceTypesAdmin(admin.ModelAdmin):
    ...


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    ...


@admin.register(ServicesRadius)
class ServicesRadiusAdmin(admin.ModelAdmin):
    ...


@admin.register(ServiceTime)
class ServiceTimeAdmin(admin.ModelAdmin):
    ...


@admin.register(Appointments)
class AppointmentsAdmin(admin.ModelAdmin):
    ...

from django.shortcuts import render
from django.http import JsonResponse
from .models import Services, ServicesTypes

def index(request):
    ServicesTypes.objects.filter(id='5fa0b233f6bb4ed38c467fd18e991c3f').delete()
    services_types = ServicesTypes.objects.all()
    res = []
    for type in services_types:
        res.append({'type_id': type.id, 'type': type.name, 'services': list(service.name for service in Services.objects.filter(type_id=type.id))})
    return JsonResponse({'services_list': res})

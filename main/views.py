from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from datetime import date

# DB services import
from .services.get_pricing_data import get_pricing_data

def product_and_service_list(request):
    # products = Products.objects.all()
    additional_services = AddotionalServices.objects.all()
    context = {
        # 'products': products,
        'additional_services': additional_services
    }
    return render(request, 'product_and_service_list.html', context)

def form_data(request):
    services_types = ServicesTypes.objects.all()
    radius = ServicesRadius.objects.all()
    res = []
    for type in services_types:
        res.append({
            'type_id': type.id, 
            'type': type.name, 
            'services': list({'id': service.id, 'name': service.name} for service in Services.objects.filter(type_id=type.id))
        })
    return JsonResponse({'services_list': res, 'radius_list': [x.radius for x in radius]})


def time_data(request, year, month, day):
    services_time = ServiceTime.objects.all()
    appointments = Appointments.objects.all()
    res = {}
    for el in services_time:
        res[el.time.strftime('%H:%M')] = True
    for el in appointments:
        if el.date == date(year, month, day):
            res[el.time.time.strftime('%H:%M')] = False

    return JsonResponse({'time': res})


def index(request):
    return render(request, 'main/index.html', {})

def form(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
    return render(request, 'main/form.html', {})

def pricing(request):
    storage = get_pricing_data(Storage)
    light_service = get_pricing_data(LightService)
    hard_service = get_pricing_data(HardService)
    full_light_service = get_pricing_data(FullLightService)
    full_hard_service = get_pricing_data(FullHardService)
    addotional_service = AddotionalServices.objects.all()
    print(addotional_service)

    return render(request, 'main/pricing.html', {
        'storage': storage,
        'light_service': light_service,
        'hard_service': hard_service,
        'full_light_service': full_light_service,
        'full_hard_service': full_hard_service,
        'addotional_service': addotional_service
    })

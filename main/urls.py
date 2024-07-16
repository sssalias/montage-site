from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('pricing', pricing, name='pricing'),
    path('form', form, name='form'),
    path('form/data/get', form_data, name='form_data'),
]

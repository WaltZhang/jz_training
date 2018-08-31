from django.urls import path

from . import viewsets


app_name = 'locations'

urlpatterns = [
    path('api/provinces/', viewsets.ProvinceList.as_view(), name='provinces'),
    path('api/provinces/<str:pcode>/', viewsets.ProvinceCities.as_view(), name='province'),
    path('api/cities/', viewsets.CityList.as_view(), name='cities'),
    path('api/provinces/<str:pcode>/<str:ccode>/', viewsets.CityDistricts.as_view(), name='city'),
    path('api/districts/', viewsets.DistrictList.as_view(), name='districts'),
]
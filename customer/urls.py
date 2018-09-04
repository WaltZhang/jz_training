from django.urls import path
from django.views.generic.base import TemplateView

from . import views, viewsets


app_name = 'customer'

urlpatterns = [
    path('register/', views.CreateCustomerView.as_view(), name='register'),
    path('identity/', views.IdentityView.as_view(), name='identity'),
    path('api/identity/', viewsets.IdentityView.as_view(), name='api_identity'),
    path('apply/', views.CreateApplyView.as_view(), name='apply'),
    path('result/', TemplateView.as_view(template_name='customer/result.html'), name='result'),
]

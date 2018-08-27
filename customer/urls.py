from django.urls import path

from . import views


app_name = 'customer'

urlpatterns = [
    path('register/', views.CreateCustomerView.as_view(), name='register'),
    path('identity/', views.IdentityView.as_view(), name='identity'),
]

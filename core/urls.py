from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('insurance/', views.insurance, name='insurance'),
    path('contact/', views.contact, name='contact'),
]

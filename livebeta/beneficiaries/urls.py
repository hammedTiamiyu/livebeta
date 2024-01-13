from django.urls import path
from . import views

urlpatterns=[
    path('', views.main, name='main'),
    path('beneficiaries/', views.beneficiaries, name='beneficiaries'),
    path('beneficiaries/details/<int:id>', views.details, name='details'),
    path('testing', views.testing, name='testing'),
]
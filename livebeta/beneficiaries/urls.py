from django.urls import path
from . import views

urlpatterns=[
    path('beneficiaries/', views.beneficiaries, name='beneficiaries')
]
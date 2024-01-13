# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Beneficiary

def beneficiaries(request):
    beneficiary_list = Beneficiary.objects.all().values()
    template = loader.get_template('all_beneficiaries.html')
    context = {
        'beneficiary_list': beneficiary_list
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    beneficiary = Beneficiary.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'beneficiary': beneficiary
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    beneficiary_list = Beneficiary.objects.values().all()
    # beneficiary_list = Beneficiary.objects.values_list('firstname')
    template = loader.get_template('template.html')
    context = {
        # 'fruits': ['Apple', 'Banana', 'Cherry'],   
        'beneficiary_list': beneficiary_list
    }
    return HttpResponse(template.render(context, request))
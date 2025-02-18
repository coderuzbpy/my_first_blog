from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse

def get_customer(request):
    return render(request, 'customer.html')

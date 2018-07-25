from django.shortcuts import render
from django.http import HttpResponse

def aguarde(request):
    return render(request, 'index.html',{})
from django.shortcuts import render
from django.http import HttpResponse
from .models import items


# Create your views here.
def home(request):
    x = items.objects.all()
    return render(request,'index.html',{'x':x})

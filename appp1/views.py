from django.shortcuts import render, HttpResponse
from .models import appp1
# Create your views here.

def funs1(request):
    allobj = appp1.objects.all()
    return render(request,'first.html', {'results' : allobj})



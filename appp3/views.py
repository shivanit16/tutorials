from django.shortcuts import render, HttpResponse

# Create your views here.

def tans1(request):
    return HttpResponse('<h1> I am  </h1>')

def tans2(request):
    return HttpResponse('<h1> good </h1>')

def tans3(request):
    return HttpResponse('<h1> boy </h1>')

from django.shortcuts import render, HttpResponse

# Create your views here.

def cans1(request):
    return HttpResponse('<h1> my </h1>')

def cans2(request):
    return HttpResponse('<h1> Name </h1>')

def cans3(request):
    return HttpResponse('<h1> is V </h1>')

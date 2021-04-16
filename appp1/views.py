from django.shortcuts import render, HttpResponse

# Create your views here.

def funs1(request):
    return HttpResponse('<h1> hello </h1>')

def funs2(request):
    return HttpResponse('<h1> how are you </h1>')

def funs3(request):
    return HttpResponse('<h1> i am fine </h1>')

from django.shortcuts import render, HttpResponse

# Create your views here.

def cans1(request):
    return render(request,'second.html')

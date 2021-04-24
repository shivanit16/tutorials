from django.shortcuts import render, HttpResponse
from .models import appp2
# Create your views here.

def cans1(request):

    if request.method == 'POST':
        Name = request.POST['name']
        Bias = request.POST['bias']
        Age = request.POST['age']
        Country = request.POST['country']

        allobj2 = appp2(Name= Name,Bias= Bias,Age=Age, Country= Country)
        allobj2.save()

    allobj2 = appp2.objects.all()
    return render(request,'second.html', {'results2' : allobj2})
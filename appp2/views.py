from django.shortcuts import render, HttpResponse
from .models import appp2
# Create your views here.

def cans1(request):

    if request.method == 'POST':
        Name = request.POST['name']
        Bias = request.POST['bias']
        Country = request.POST['country']
        print(Name)
        print(Bias)

        allobj2 = appp2(Name= Name,Bias= Bias)
        allobj2.save()

    allobj2 = appp2.objects.all()
    return render(request,'second.html', {'results2' : allobj2})
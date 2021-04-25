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

def cans2(request):
    if request.method == 'POST':
        search = request.POST['search']

        try :
            searchobj = appp2.objects.get(Name=search)
            searchobj2 = dict(Name= searchobj.Name,Bias= searchobj.Bias,Age=searchobj.Age, Country= searchobj.Country)
            context = {'finf' : searchobj2}

        except Exception as e:
            print(e)
            novalue = "invalid"
            context = {'none' : novalue}

        return render(request,'finf.html', context=context)


    return render(request,'finf.html')


def cans3(request):
    return render(request,'finf.html')


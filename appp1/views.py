from django.shortcuts import render, HttpResponse
from .models import appp1
# Create your views here.

def funs1(request):
    results =list()
    allobj = appp1.objects.all()
    a = appp1(Name="Kim Taehyung")
    for i in allobj:
        each = dict(Name=i.Name, StageName=i.StageName, Songs=i.Songs)
        results.append(each)
    print (results)
    context = {'appp1' : results}
    return render(request,'first.html', context = context)



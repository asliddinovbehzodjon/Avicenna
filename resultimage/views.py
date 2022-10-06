from django.shortcuts import render
from teacher.models import BlokTestlar
from json import dumps
# Create your views here.
def home(request):
    data1  = BlokTestlar.objects.filter(week_code=8898).only('ball')
    data2 = BlokTestlar.objects.filter(week_code=8883).only('ball')
    a = []
    b = []
    for i in data1:
        a.append(i.ball)
    for k in data2:
        b.append(k.ball)
    a = dumps(a)
    b = dumps(b)
    context = {
        'data1':a,
        'data2':b
    }
    print(a,b)
    return render(request,'index.html',context)
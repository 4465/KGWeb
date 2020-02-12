from TestModel.models import *
from django.shortcuts import render,redirect


def SelectALL(request):
    data = Main.objects.all()
    # print(data)
    return render(request, 'index.html', {'data': data})


def Select(request):
    hero = request.GET['Hero']
    print(hero)
    relation = request.GET['Relations']
    print(relation)
    result = Main.objects.filter(subject=hero, predicate=relation).order_by("id")
    print(result)
    return render(request, 'index.html', {'result': result})


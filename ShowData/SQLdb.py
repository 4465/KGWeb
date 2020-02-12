from TestModel.models import *
from django.shortcuts import render,redirect
from Database.DB import DB

def SelectALL(request):
    data = Main.objects.all()
    # print(data)
    return render(request, 'index.html', {'data': data})


def Select(request):
    sql = request.GET['Sql']
    print(sql)
    # hero = request.GET['Hero']
    # print(hero)
    # relation = request.GET['Relations']
    # print(relation)
    if sql.strip() == ' ':
        print("sql is null")
    else:
        db = DB()
        result = db.Select(sql)
        print(result)
        for i in result:
            print(i)
        return render(request, 'index.html', {'result': result})
        # for i in result:
        #     print(i)
    # result = Main.objects.filter(subject=hero, predicate=relation).order_by("id")
    # print(result)

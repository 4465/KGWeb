from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'hello world'
    return render(request, 'hello.html', context)


def Index(request):
    context = {}
    return render(request, 'index.html', context)

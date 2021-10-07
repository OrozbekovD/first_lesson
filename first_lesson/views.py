from django.shortcuts import render


def index(request):
    name = 'Orozbekov Dosoy'
    return render(request, 'index.html', locals())


def index2(request):
    name = 'Kuttubekov Emir'
    return render(request, 'index2.html', locals())


def index3(request):
    name = 'Abakirov Joomart'
    return render(request, 'index3.html', locals())


def index4(request):
    name = 'Satyndiev Jayil'
    return render(request, 'index4.html', locals())


def index5(request):
    name = 'Belekov Nurs'
    return render(request, 'index5.html', locals())

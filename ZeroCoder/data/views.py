from django.shortcuts import render
from django.http import HttpResponse

def data(request):
        return HttpResponse("<h1>Эта страница с данными о моем первом проекте на Django</h1>")

def test(request):
    return HttpResponse("<h1>Это страница с тестами моего проекта на Django</h1>")


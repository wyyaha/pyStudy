from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("欢迎使用django")

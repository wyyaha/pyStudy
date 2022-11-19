from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("欢迎使用django")


def user_list(request):
    return render(request, 'user_list.html')

def user_add(request):
    return HttpResponse('添加用户')
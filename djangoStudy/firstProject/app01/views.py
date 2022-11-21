import json
import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("欢迎使用django")


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return HttpResponse('添加用户')


def tpl(request):
    name = "王丫"
    roles = ["管理员", "保安"]
    tels = {"w": "apple", "d": "banana"}
    return render(request, 'tpl.html', {'n1': name, 'roles': roles, 'tels': tels})


def news(request):
    headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
    res1 = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/11/news")
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/11/news", "headers"= headers)
    print(res.text)
    # data_list = res.json()
    # print(data_list)
    return render(request, 'news.html')
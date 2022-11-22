import json
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01.models import UserInfo,Department

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
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/11/news", headers=headers)
    data_list = res.json()
    return render(request, 'news.html', {'data_list': data_list})


def something(request):
    # request是一个对象，封装了所有用户发过来的数据
    print(request.GET)
    return HttpResponse("返回内容")


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    if username == "root" and pwd == "123":
        return redirect("https://www.baidu.com")
    else:
        error_msg = "登录失败"
        return render(request, 'login.html', {'error_msg': error_msg})


def orm(request):
    Department.objects.create(title="销售部")
    Department.objects.create(title="IT部")
    Department.objects.create(title="运营部")

    UserInfo.objects.create(name="武松", password="123", age=12)
    UserInfo.objects.create(name="朱2", password="456", age=23)
    UserInfo.objects.create(name="武大朗", password="123", age=40)

    # UserInfo.objects.filter(id=5).delete()
    # UserInfo.objects.all().delete()

    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.name, obj.password)

    # 返回数据格式为对象
    # firstUser = UserInfo.objects.filter(id=7).first()
    # print(firstUser.name, firstUser.password)

    updateUser = UserInfo.objects.all().update(password=668)
    print(updateUser)
    return HttpResponse("操作数据库成功")
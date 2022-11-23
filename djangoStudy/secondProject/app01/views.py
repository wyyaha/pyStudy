from django.shortcuts import render, redirect

from app01 import models
from app01.models import Department, UserInfo


# Create your views here.
def depart_list(request):
    department_list = Department.objects.all()
    return render(request, 'depart_list.html', {'department_list': department_list})


def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    title = request.POST.get("title")
    Department.objects.create(title=title)
    return redirect("/depart/list")


def depart_delete(request):
    did = request.GET.get("did")
    Department.objects.filter(id=did).delete()
    return redirect("/depart/list")


def depart_edit(request, did):
    if request.method == 'GET':
        depart_info = Department.objects.filter(id=did).first()
        return render(request, 'depart_edit.html', {'depart_info': depart_info})
    # did = request.POST.get("id")
    title = request.POST.get("title")
    Department.objects.filter(id=did).update(title=title)
    return redirect("/depart/list")


def user_list(request):
    user_list = UserInfo.objects.all()
    return render(request, 'user_list.html', {'user_list': user_list})


def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choice': UserInfo.gender_choices,
            'depart_choice': Department.objects.all()
        }
        return render(request, 'user_add.html', context)

    name = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')
    account = request.POST.get('account')
    create_time = request.POST.get('create_time')
    gender = request.POST.get('gender')
    depart = request.POST.get('depart')
    print(gender, depart)
    Department.objects.create(name=name, password=password, age=age,
                              account=account, create_time=create_time,
                              gender=gender, department_id=depart)

    return(redirect("/user/list/"))





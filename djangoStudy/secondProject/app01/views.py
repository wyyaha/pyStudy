from django.shortcuts import render, redirect

from app01 import models
from app01.models import Department


# Create your views here.
def depart_list(request):
    department_list = Department.objects.all()
    return render(request, 'test.html', {'department_list': department_list})


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

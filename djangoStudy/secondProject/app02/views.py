from django.shortcuts import render, redirect

from app02 import models
from app02.models import Department, UserInfo, PrettyNum
from django import forms


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

    return redirect("/user/list/")


class UserModelForm(forms.ModelForm):
    # name = forms.CharField(min_length=2)
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "department"]
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"})
        #
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_model_form_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/user/list/")
    else:
        # print(form.errors)
        return render(request, 'user_model_form_add.html', {"form": form})


def user_edit(request, uid):
    row_object = UserInfo.objects.filter(id=uid).first()
    if request.method == 'GET':
        # 这里是ModelForm的语法，加上instance数据后，会显示这一行的数据
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {"form": form})
    # 这里不加instance（表示当前操作对象）的话，则为新增
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 如果想要向数据库添加额外数据，可以
        # form.instance.数据库字段名 = 值
        form.save()
        return redirect("/user/list/")
    else:
        # print(form.errors)
        return render(request, 'user_model_form_add.html', {"form": form})


def user_delete(request, uid):
    UserInfo.objects.filter(id=uid).delete()
    return redirect('/user/list/')


def pretty_list(request):
    queryset = PrettyNum.objects.all().order_by("-level")
    return render(request, 'pretty_list.html', {'queryset': queryset})


from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class PrettyModelForm(forms.ModelForm):
    # 给用户提交的数据添加验证有两种方法，方法一：
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误')],
    # )
    class Meta:
        model = models.PrettyNum
        # fields = "__all__" #展示数据库的所有列
        fields = ["mobile", "price", "level", "status"]
        # exclude = ['level'] #展示除了level列的所有列
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"})
        #
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    # 给用户提交的数据添加验证，方法二：
    def clean_mobile(self):
        text_mobile = self.cleaned_data['mobile']
        # 验证不通过
        # if len(text_mobile) != 11:
        #     raise ValidationError('格式错误')
        # 手机号不能重复
        exists = PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=text_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在')
        # 验证通过
        return text_mobile


def pretty_add(request):
    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/pretty/list/")
    else:
        # print(form.errors)
        return render(request, 'pretty_add.html', {"form": form})


def pretty_edit(request, pid):
    row_object = PrettyNum.objects.filter(id=pid).first()
    if request.method == 'GET':
        # 这里是ModelForm的语法，加上instance数据后，会显示这一行的数据
        form = PrettyModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', {"form": form})
    # 这里不加instance（表示当前操作对象）的话，则为新增
    form = PrettyModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 如果想要向数据库添加额外数据，可以
        # form.instance.数据库字段名 = 值
        form.save()
        return redirect("/pretty/list/")
    else:
        return render(request, 'pretty_edit.html', {"form": form})


def pretty_delete(request, pid):
    PrettyNum.objects.filter(id=pid).delete()
    return redirect('/pretty/list/')

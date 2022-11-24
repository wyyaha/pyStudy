from django.db import models


# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    """
        insert into app02_userinfo(name, password, age, account, create_time, gender, department_id) values("韩寒", "123", 24, 100.66, "2020-02-28", 2, 1);
        insert into app02_userinfo(name, password, age, account, create_time, gender, department_id) values("李梅", "123", 43, 100.66, "2020-02-28", 1, 2);
        insert into app02_userinfo(name, password, age, account, create_time, gender, department_id) values("王丫", "123", 12, 100.66, "2020-02-28", 2, 1);
    """
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    # max_digits 数字允许的最大位数，decimal_places 小数的最大位数
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name="入职时间")
    # on_delete=models.CASCADE表示级联删除
    department = models.ForeignKey(verbose_name="部门", to='Department', to_field="id", on_delete=models.CASCADE)
    # on_delete=models.SET_NULL表示部门表数据被删除时，这一列数据为空
    # department = models.ForeignKey(to="Department", to_fields="id", null=True, blank=True, on_delete=models.SET_NULL)
    gender_choices = (
        (1, "男"),
        (2, "女")
    )
    # django做的约束,性别只能为男和女
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class PrettyNum(models.Model):
    """
    靓号表
     insert into app02_prettynum(mobile, price, level, status) values("15617822301", 21, 1, 1);
     insert into app02_prettynum(mobile, price, level, status) values("15617822302", 34, 2, 2);
     insert into app02_prettynum(mobile, price, level, status) values("15617822303", 28, 3, 1);
    """
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格", default=0)
    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    status_choices = (
        (1, "已占用"),
        (2, "未使用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)

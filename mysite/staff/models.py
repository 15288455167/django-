from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Admin(models.Model):
    username = models.CharField(verbose_name="姓名", max_length=64)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    '''部门表'''
    title = models.CharField(verbose_name='部门名称', max_length=20)

    def __str__(self):
        return self.title


class staff_auth(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名', max_length=20)
    password = models.CharField(verbose_name='密码', max_length=20)
    age = models.IntegerField(verbose_name='年龄')
    salary = models.DecimalField(verbose_name='薪水', max_digits=10, decimal_places=2, default=0)
    entry_time = models.DateTimeField(verbose_name='入职时间')
    gender_choice = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choice)
    department = models.ForeignKey(verbose_name='关联部门', to='Department', to_field='id', on_delete=models.CASCADE)


class Pretty_auth(models.Model):
    '''靓号管理'''
    moblie = models.CharField(verbose_name="手机号码", max_length=11, )
    price = models.DecimalField(verbose_name="价格", max_digits=20, decimal_places=2, default=0)
    level_choices = (
        (1, "初级"),
        (2, "中级"),
        (3, "高级"),
    )
    level = models.SmallIntegerField(verbose_name="等级", choices=level_choices)
    status_choices = (
        (1, "已占用"),
        (2, "未占用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)


class Task_list(models.Model):
    level_choice = (
        (1, '日常'),
        (2, '重要'),
        (3, '紧急'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choice, default=1)
    title = models.CharField(verbose_name='标题', max_length=64)
    detail = models.CharField(verbose_name='任务详情', max_length=64)
    charge = models.ForeignKey(verbose_name='负责人', to=Admin, on_delete=models.CASCADE)


class Order(models.Model):
    order_num = models.CharField(verbose_name='订单编号', max_length=64)
    order_name = models.CharField(verbose_name='商品名称', max_length=64)
    order_price = models.DecimalField(verbose_name='价格', max_digits=10, decimal_places=2)
    status_choice = (
        (1, '待支付'),
        (2, '已支付'),
    )
    order_status = models.SmallIntegerField(verbose_name='商品状态', choices=status_choice, default=1)
    order_auth = models.ForeignKey(verbose_name='管理员', to='Admin', on_delete=models.CASCADE)

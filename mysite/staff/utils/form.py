from django import forms
from staff import models


from staff.utils.bootstrap import BootstrapModelform
from staff.utils.encrpy import md5

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from staff.utils.bootstrap import Bootstrapform


class Pretty_edit(BootstrapModelform):
    moblie = forms.CharField(
        label='手机号码',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式错误', )],
    )

    class Meta:
        model = models.Pretty_auth
        fields = ['moblie', 'price', 'level', 'status']


class Pretty_num(BootstrapModelform):
    moblie = forms.CharField(
        label='手机号码',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式错误', )],
    )

    class Meta:
        model = models.Pretty_auth
        fields = ['moblie', 'price', 'level', 'status']


class AuthModel(BootstrapModelform):
    class Meta:
        model = models.staff_auth
        fields = ['name', 'password', 'age', 'salary', 'entry_time', 'gender', 'department']


class Admin_edit(BootstrapModelform):

    password = forms.CharField(
        label="密码",
        widget= forms.PasswordInput
    )

    class Meta:
        model = models.Admin()
        fields = ['username', 'password']


class Admin_add(BootstrapModelform):

    confirm = forms.CharField(
        label="确认密码",
        widget= forms.PasswordInput
    )

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm']
        widgets = {
            'password': forms.PasswordInput
        }


    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


    def clean_confirm(self):
        print(self.cleaned_data)
        password = self.cleaned_data.get('password')
        conf = md5(self.cleaned_data.get('confirm'))
        if password != conf:
            raise ValidationError("两次密码不一致！")
        else:
            return conf


class Admin_reset(BootstrapModelform):

    confirm = forms.CharField(
        label="确认密码",
        widget= forms.PasswordInput
    )

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm']
        widgets = {
            'password': forms.PasswordInput
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        md5_pwd = md5(pwd)
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError('不能与之前的密码相同')
        return md5_pwd


    def clean_confirm(self):
        print(self.cleaned_data)
        password = self.cleaned_data.get('password')
        conf = md5(self.cleaned_data.get('confirm'))
        if password != conf:
            raise ValidationError("两次密码不一致！")
        else:
            return conf


class Acount(Bootstrapform):
    username = forms.CharField(
        label="用户名",
        widget= forms.TextInput(attrs={"class": "form-control"}),
    )

    password = forms.CharField(
        label="密码",
        widget= forms.PasswordInput(attrs={"class": "form-control"}) ,
    )

    vericode = forms.CharField(
        label="验证码",
        widget= forms.TextInput(attrs={"class": "form-control"}) ,
    )



    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


class Task_auth(BootstrapModelform):

    class Meta:
        model = models.Task_list
        fields = '__all__'


class Order_list(BootstrapModelform):
    class Meta:
        model = models.Order
        fields = '__all__'
        exclude = ['order_num', 'order_auth']







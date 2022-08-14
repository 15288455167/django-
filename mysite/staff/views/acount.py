from django.shortcuts import render, redirect
from staff.utils.form import Acount
from django.core.exceptions import ValidationError
from staff import models
from django.shortcuts import HttpResponse
from staff.utils.code import check_code
from io import BytesIO


def login(request):
    if request.method == 'GET':
        form = Acount()
        return render(request, 'login.html', {"form": form})
    else:
        form = Acount(data=request.POST)
        if form.is_valid():

            input_code = form.cleaned_data.pop('vericode')
            cor_code = request.session.get('image_code', '')
            if input_code.upper() != cor_code.upper():
                form.add_error('vericode', "验证码错误")
                return render(request, 'login.html', {"form": form})

            admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
            if not admin_object:
                form.add_error('password', "用户名或密码错误")
                return render(request, 'login.html', {"form": form})
            request.session['info'] = {"id": admin_object.id, 'name': admin_object.username}
            request.session.set_expiry(60*60*24*7)
            return redirect('/admin/list/')
        return render(request, 'login.html', {"form": form})


def logout(request):
    request.session.clear()
    return redirect('/login/')


def image_code(request):
    img, code_string = check_code()

    request.session['image_code'] = code_string
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')

    return HttpResponse(stream.getvalue())

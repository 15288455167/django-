from staff import models

from django.shortcuts import render, redirect
from django import forms

from staff.utils.pagination import Pagination
from staff.utils.form import Admin_edit, Admin_add, Admin_reset


def admin_list(request):

    queryset = models.Admin.objects.all()

    page_object = Pagination(request, queryset)

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }

    return render(request, "admin_list.html", context)


def admin_edit(request, nid):
    data = models.Admin.objects.filter(id=nid).first()
    if request.method == "GET":
        form = Admin_edit(instance=data)
        return render(request, 'admin_edit.html', {"form": form})
    else:
        form = Admin_edit(data=request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/admin/list')
        else:
            return render(request, 'admin_edit.html', {"form": form})


def admin_delete(requset, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')


def admin_add(request):
    if request.method == 'GET':
        form = Admin_add()
        return render(request, 'add.html', {"form": form, "title": "新建管理员"})
    else:
        form = Admin_add(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/admin/list/')
        else:
            return render(request, 'add.html', {"form": form, "title": "新建管理员"})


def admin_reset(request, nid):
    data = models.Admin.objects.filter(id=nid).first()
    title = "重置密码——{}".format(data.username)
    if request.method == 'GET':
        form = Admin_reset(instance=data)
        return render(request, 'add.html', {"form": form, "title": title})
    else:
        form = Admin_reset(data=request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/admin/list/')
        else:
            return render(request, 'add.html', {"form": form, "title": title})



































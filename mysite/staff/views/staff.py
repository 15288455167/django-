from django.shortcuts import render, redirect
from staff import models
from staff.utils.pagination import Pagination
from staff.utils.form import AuthModel


# 员工管理
def staff_list(request):
    queryset = models.staff_auth.objects.all()

    page_object = Pagination(request, queryset)
    context = {
        "queryset": queryset,
        "page_string": page_object.html(),
    }

    return render(request, 'staff_list.html', context)


def add_staff(request):
    if request.method == "GET":
        form = AuthModel()
        return render(request, 'add_staff.html', {"form": form})
    else:
        form = AuthModel(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/staff/list')
        else:
            return render(request, 'add_staff.html', {"form": form})


def staff_edit(request, nid):
    data = models.staff_auth.objects.filter(id=nid).first()
    if request.method == "get":
        form = AuthModel(instance=data)
        return render(request, 'staff_edit.html', {"form": form})
    else:
        form = AuthModel(data=request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/staff/list/')
        else:
            return render(request, 'staff_edit.html', {"form": form})


def staff_delete(request, nid):
    models.staff_auth.objects.filter(id=nid).delete()
    return redirect('/staff/list')
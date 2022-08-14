from django.shortcuts import render, redirect
from staff import models
from staff.utils.pagination import Pagination


def department_list(request):
    queryset = models.Department.objects.all()

    page_object = Pagination(request, queryset)
    context = {
        'queryset': queryset,
        'page_string': page_object.html(),
    }

    return render(request, 'department_list.html', context)


def add_department(request):
    if request.method == "GET":
        return render(request, 'add_department.html')
    else:
        title = request.POST.get('title')
        models.Department.objects.create(title=title)
        return redirect('/department/list/')


def delete_department(request):
    nid = request.GET.get('nid')  # 获取nid
    models.Department.objects.filter(id=nid).delete()  # 删除部门
    return redirect('/department/list/')


def department_edit(request, nid):
    if request.method == "GET":
        department_msg = models.Department.objects.filter(id=nid).first()
        return render(request, 'department_edit.html', {"department_msg": department_msg})

    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/department/list')

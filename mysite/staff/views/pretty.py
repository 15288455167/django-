from django.shortcuts import render, redirect
from staff import models
from staff.utils.pagination import Pagination
from staff.utils.form import Pretty_edit, Pretty_num
from django import forms


def pretty_auth(request):
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['moblie__contains'] = search_data

    queryset = models.Pretty_auth.objects.filter(**data_dict).order_by('-price')
    page_object = Pagination(request, queryset)

    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }

    return render(request, 'pretty_auth.html', context)


def add_num(request):
    if request.method == 'GET':
        form = Pretty_num()
        return render(request, 'add_num.html', {"form": form})
    else:
        form = Pretty_num(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/pretty/auth')
        else:
            return render(request, 'add_num.html', {"form": form})


def pretty_edit(request, nid):
    data = models.Pretty_auth.objects.filter(id=nid).first()
    if request.method == "GET":
        form = Pretty_edit(instance=data)
        return render(request, 'pretty_edit.html', {"form": form})
    else:
        form = Pretty_edit(data=request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/pretty/auth')
        else:
            return render(request, 'pretty_edit.html', {"form": form})


def pretty_delete(request, nid):
    models.Pretty_auth.objects.filter(id=nid).delete()
    return redirect('/pretty/auth')

from django.shortcuts import render, redirect, HttpResponse
import json
from staff.utils.form import Order_list
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django import forms
import random
from datetime import datetime
from staff.utils.pagination import Pagination
from staff import models


def order_list(request):
    queryset = models.Order.objects.all()
    form = Order_list

    page_objects = Pagination(request, queryset)
    context = {
        "queryset": page_objects.page_queryset,
        "page_string": page_objects.html(),
        "form": form,
    }

    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    # {'level': ['1'], 'title': ['sdfsdfsdfsd'], 'detail': ['111'], 'user': ['8']}
    # print(request.POST)

    # 1.用户发送过来的数据进行校验（ModelForm进行校验）
    form = Order_list(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.instance.order_num = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        form.instance.order_auth_id = request.session['info']['id']
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))


def order_delete(request):
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "数据不存在"})

    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def order_detail(request):
    uid = request.GET.get('uid')
    row_dict = models.Order.objects.filter(id=uid).values('order_name', 'order_status', 'order_price').first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})

    result = {
        "status": True,
        "data": row_dict
    }
    return JsonResponse(result)


@csrf_exempt
def order_edit(request):
    """ 编辑订单 """
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, 'tips': "数据不存在，请刷新重试。"})

    form = Order_list(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})

    return JsonResponse({"status": False, 'error': form.errors})














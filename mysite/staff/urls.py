from django.urls import path, include
from staff.views import department, pretty, staff, admin, acount, task, order, chart, upload

urlpatterns = [
    path('department/list/', department.department_list),
    path('add/department/', department.add_department),
    path('delete/department/', department.delete_department),
    path('department/<int:nid>/edit/', department.department_edit),

    # 员工管理
    path('staff/list/', staff.staff_list),
    path('add/staff/', staff.add_staff),
    path('staff/<int:nid>/edit/', staff.staff_edit),
    path('staff/<int:nid>/delete/', staff.staff_delete),

    # 靓号管理
    path('pretty/auth/', pretty.pretty_auth),
    path('add/num/', pretty.add_num),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),

    # 管理员
    path('admin/list/', admin.admin_list),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),
    path('admin/add/', admin.admin_add),

    #登录界面
    path('login/', acount.login),
    path('logout/', acount.logout),
    path('image/code/', acount.image_code),

    # 任务管理
    path('task/list/', task.task_list),
    path('task/add/', task.task_add),

    # 订单管理
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    # 数据可视化
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),

    # 文件上传
    path('upload/list/', upload.upload_list),
]

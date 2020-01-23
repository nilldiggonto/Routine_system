from django.urls import path
from .views import (homepage,all_dept,create_depart,update_dept,delete_dept,
                    all_teacher,create_teacher,update_teacher,delete_teacher,days_table,
                    times_table,display_routine,create_routine,update_routine,delete_routine )

app_name = 'admin_page'

urlpatterns = [
    path('',homepage,name='admin-home'),
    path('admin/department/',all_dept,name='admin-dept'),
    path('admin/teacher/',all_teacher,name='admin-teacher'),
    path('admin/create/department/',create_depart,name='admin-dept-create'),
    path('admin/create/teacher/',create_teacher,name='admin-teacher-create'),
    path('admin/routine/days/',days_table,name='admin-routine-days'),
    path('admin/routine/times/',times_table,name='admin-routine-times'),
    path('admin/routine/display_routine/',display_routine,name='admin-routine-display'),
    path('admin/routine/create/room/',create_routine,name='admin-room-create'),

    path('admin/update/department/<int:id>/',update_dept,name='admin-dept-update'),
    path('admin/delete/department/<int:id>/',delete_dept,name='admin-dept-delete'),
    path('admin/update/teacher/<int:id>/',update_teacher,name='admin-teacher-update'),
    path('admin/delete/teacher/<int:id>/',delete_teacher,name='admin-teacher-delete'),
    path('admin/update/routine/<int:id>/',update_routine,name='admin-routine-update'),
    path('admin/delete/routine/<int:id>/',delete_routine,name='admin-routine-delete'),


]
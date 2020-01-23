from django.urls import path,include
from .views import home,all_dept,dept_teacher,teacher_detail,all_teacher

app_name= 'allinfo'

urlpatterns = [
    path('',home,name='home'),
    path('dept/',all_dept,name='dept'),
    path('all/teacher/',all_teacher,name='all_teach'),
    path('teacher/<int:id>/',dept_teacher,name='dept_tech'),
    path('detail/teacher/<int:id>/',teacher_detail,name='tech_detail'),
    
]

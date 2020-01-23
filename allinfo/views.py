from django.shortcuts import render,get_object_or_404,redirect
from .models import All_department,Techer_info
from routine_info.models import Room_with_na
from django.db.models import Q
# Create your views here.

def home(request):
    template_name ='home.html'
    return render(request,template_name)

def all_dept(request):
    template_name = 'allinfo/all_dept.html'
    all_dept = All_department.objects.all()
    context = {
        'all_dept': all_dept,
    }
    return render(request,template_name,context)


def dept_teacher(request,id):
    template_name   = 'allinfo/teach_list.html'
    category = get_object_or_404(All_department, id=id)
    
    queryset = Techer_info.objects.filter(dept_belong=category.id)

   
    

    context = {
        'category': category,
        'object_list':queryset,
        # 'cobject_list':c_queryset,
        # 'page_request_var':page_request_var,
    }
    return render(request,template_name,context)





def teacher_detail(request,id):
    template_name   = 'allinfo/teach_detail.html'
    queryset = get_object_or_404(Techer_info, id=id)
    routine_time = Room_with_na.objects.filter(teacher_initial=queryset.id)
    
    print(routine_time)
    # print(saturday_time)
    # print(saturday_time)
    for saturday in routine_time:
        print(saturday.routine_days)
        print(str(saturday.routine_days))
        

    # queryset = Techer_info.objects.filter(dept_belong=category.id)

   
    

    context = {
        # 'category': category,
        'object':queryset,
        'routine_time':routine_time,
        # 'cobject_list':c_queryset,
        # 'page_request_var':page_request_var,
    }
    return render(request,template_name,context)


def all_teacher(request):
    template_name = 'allinfo/all_tech.html'
    queryset = Techer_info.objects.all()
    query = request.GET.get('q')
    print(query)
    if query:
        queryset = queryset.filter(
            Q(name_initial__icontains=query)).distinct()

    context = {
        'object_list':queryset
    }
    return render(request,template_name,context)
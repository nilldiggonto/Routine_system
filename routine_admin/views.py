from django.shortcuts import render,redirect,get_object_or_404
from allinfo.models import All_department,Techer_info
from allinfo.forms import DepartmentForm , TeacherinfoForm
from django.contrib import messages
from routine_info.forms import RoutineDaysForm,RoutineTimeForm,RoutineTimeWithInitial
from routine_info.models import Room_with_na,Routine_days,Routine_time
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
@staff_member_required
def homepage(request):
    template_name = "routine_admin/home.html"
    all_teacher = Techer_info.objects.all().count()
    all_department = All_department.objects.all().count()
    all_routine = Room_with_na.objects.all().count()
    
    context = {
        'all_teacher': all_teacher,
        'all_department': all_department,
        'all_routine': all_routine,
    }
    return render(request,template_name,context)

@staff_member_required
def all_dept(request):
    template_name = "routine_admin/department/all_dept.html"
    all_dept = All_department.objects.all()

    

    context = {
        'all_dept': all_dept,
        
    }
    return render(request,template_name,context)

@staff_member_required
def create_depart(request):
    template_name = "routine_admin/department/create_dept.html"
    if request.method == 'POST':
        #get from values
        title = request.POST['title']
        name = request.POST['name']


        dept = All_department.objects.create(title=title,name=name)
                       
        dept.save()
        messages.success(request,'Department Created')
        return redirect('admin_page:admin-dept')
    
    context ={
        'value': 'Create',
    }

       
    
    return render(request,template_name,context)

@staff_member_required
def update_dept(request,id):
    template_name = "routine_admin/department/create_dept.html"
    instance = get_object_or_404(All_department,id=id)

    if request.method == 'POST':
        #get from values
        title = request.POST['title']
        name = request.POST['name']


        dept = All_department.objects.create(title=title,name=name)
                       
        dept.save()
        messages.success(request,'Department Updated')
        return redirect('admin_page:admin-dept')

    context = {
        'instance':instance,
        'value': 'Update',
    }
    return render(request,template_name,context)

@staff_member_required
def delete_dept(request,id):
    # template_name = "routine_admin/department/all_dept.html"
    instance = get_object_or_404(All_department,id=id)
    instance.delete()
    messages.warning(request,'Department Deleted')
    return redirect('admin_page:admin-dept')


############### Teacher info Section ######
@staff_member_required
def all_teacher(request):
    template_name = "routine_admin/teacher/all_teacher.html"
    all_teach = Techer_info.objects.all()

    

    context = {
        'all_teach': all_teach,
        
    }
    return render(request,template_name,context)

@staff_member_required
def create_teacher(request):
    template_name = "routine_admin/teacher/create_teacher.html"
    all_dept = All_department.objects.all()
    form = TeacherinfoForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.user   = request.user
        instance.save()
        return redirect('admin_page:admin-teacher')
    
    context ={
        'value': 'Create',
        'all_dept':all_dept,
        'form':form
    }

       
    
    return render(request,template_name,context)


@staff_member_required
def update_teacher(request,id):
    template_name = "routine_admin/teacher/create_teacher.html"
    instance = get_object_or_404(Techer_info,id=id)
    form = TeacherinfoForm(request.POST or None,instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        
        instance.save()
        return redirect('admin_page:admin-teacher')
    
    context ={
        'value': 'update',
        
        'form':form,
    }

       
    
    return render(request,template_name,context)


@staff_member_required
def delete_teacher(request,id):
    # template_name = "routine_admin/department/all_dept.html"
    instance = get_object_or_404(Techer_info,id=id)
    instance.delete()
    messages.warning(request,'Department Deleted')
    return redirect('admin_page:admin-teacher')


# Create days
@staff_member_required
def days_table(request):
    template_name = "routine_admin/routine/days/day.html"
    all_days = Routine_days.objects.all()

    context = {
        'all_days': all_days,
    }
    return render(request,template_name,context)


# Create Time
@staff_member_required
def times_table(request):
    template_name = 'routine_admin/routine/times/time.html'
    all_times = Routine_time.objects.all()

    context = {
        'all_times': all_times,
    }
    return render(request,template_name,context)


# Create routine with Initial
@staff_member_required
def display_routine(request):
    template_name = 'routine_admin/routine/routine.html'
    all_routine = Room_with_na.objects.all()

    context = {
        'all_routine' : all_routine,
    }
    return render(request,template_name,context)


@staff_member_required
def create_routine(request):
    template_name = "routine_admin/routine/create_routine.html"
    # all_dept = All_department.objects.all()
    form = RoutineTimeWithInitial(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.user   = request.user
        instance.save()
        return redirect('admin_page:admin-routine-display')
    
    context ={
        'value': 'Create',
        
        'form':form,
    }
    return render(request,template_name,context)


@staff_member_required
def update_routine(request,id):
    template_name = "routine_admin/routine/create_routine.html"
    instance = get_object_or_404(Room_with_na,id=id)
    form = RoutineTimeWithInitial(request.POST or None,instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        
        instance.save()
        return redirect('admin_page:admin-routine-display')
    
    context ={
        'value': 'update',
        
        'form':form,
    }

       
    
    return render(request,template_name,context)


@staff_member_required
def delete_routine(request,id):
    # template_name = "routine_admin/department/all_dept.html"
    instance = get_object_or_404(Room_with_na,id=id)
    instance.delete()
    messages.warning(request,'Routine Deleted')
    return redirect('admin_page:admin-routine-display')
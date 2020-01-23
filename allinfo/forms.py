from .models import All_department,Techer_info
from django import forms


class DepartmentForm(forms.ModelForm):
    
    class Meta:
        model = All_department
        fields = (
            'title',
            'name'
            
           
        )


class TeacherinfoForm(forms.ModelForm):

    class Meta:
        model = Techer_info
        fields = (
            'dept_belong',
            'name_initial',
            'name',
            'description',
            'image',
            'designation',
            'faculty',
            'email_info',
            'phone'
        )
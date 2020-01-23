from .models import Routine_days,Routine_time,Room_with_na
from django import forms


class RoutineDaysForm(forms.ModelForm):
    
    class Meta:
        model = Routine_days
        fields = (
            'days',
            
            
           
        )



class RoutineTimeForm(forms.ModelForm):
    
    class Meta:
        model = Routine_time
        fields = (
            'time_days',
            
            
           
        )



class RoutineTimeWithInitial(forms.ModelForm):
    
    class Meta:
        model = Room_with_na
        fields = (
            'teacher_initial',
            'routine_days',
            'routine_time',
            'room_no',
            
            
           
        )

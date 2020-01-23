from django.db import models
from allinfo.models import Techer_info
from django.urls import reverse
# Create your models here.

class Routine_days(models.Model):
    days        = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at  = models.DateTimeField(auto_now=True, verbose_name="Updated at")


    def __str__(self):
        return self.days


class Routine_time(models.Model):

    time_days   = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at  = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.time_days


class Room_with_na(models.Model):
    teacher_initial     = models.ForeignKey(Techer_info,on_delete=models.CASCADE, null=True, blank=True)
    routine_days        = models.ForeignKey(Routine_days,on_delete=models.CASCADE, null=True, blank=True)
    routine_time        = models.ForeignKey(Routine_time,on_delete=models.CASCADE, null=True, blank=True)
    room_no             = models.CharField(max_length=120)
    created_at          = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at          = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.room_no
    
    def get_absolute_url(self):
        return reverse("admin_page:admin-routine-update", kwargs={"id": self.id})

    def delete_get_absolute_url(self):
        return reverse("admin_page:admin-routine-delete", kwargs={"id": self.id})
    
    
    



    

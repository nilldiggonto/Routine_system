from django.db import models
from django.urls import reverse
import os,random
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext  = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,2141512411)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)

    return 'routine_system/{new_filename}/{final_filename}'.format(new_filename=new_filename,final_filename=final_filename)

class All_department(models.Model):
    title       = models.CharField(max_length=10)
    name        = models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at  = models.DateTimeField(auto_now=True, verbose_name="Updated at")


    def get_absolute_url(self):
        return reverse("allinfo:dept_tech", kwargs={"id": self.id})

    def admin_absolute_url(self):
        return reverse('admin_page:admin-dept-update', kwargs={"id":self.id})

    def admin_dept_delete(self):
        return reverse('admin_page:admin-dept-delete',kwargs={"id":self.id})
    


    def __str__(self):
        return self.title



class Techer_info(models.Model):
    dept_belong     = models.ForeignKey(All_department,on_delete=models.CASCADE, null=True, blank=True)
    name_initial    = models.CharField(max_length=10,unique=True)
    name            = models.CharField(max_length=50)
    description     = models.TextField(null=True,blank=True)
    image           = models.ImageField(upload_to=upload_image_path, null=True,blank=True)
    designation     = models.CharField(max_length=120)
    faculty         = models.CharField(max_length=120)
    email_info      = models.CharField(max_length=120)
    phone           = models.CharField(max_length=120)


    def get_absolute_url(self):
        return reverse("allinfo:tech_detail", kwargs={"id": self.id})

    def admin_get_absolute_url(self):
        return reverse("admin_page:admin-teacher-update", kwargs={"id": self.id})

    def admin_delete_get_absolute_url(self):
        return reverse("admin_page:admin-teacher-delete", kwargs={"id": self.id})
    
    
    


    def __str__(self):
        return self.name_initial
    


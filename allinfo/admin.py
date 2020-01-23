from django.contrib import admin
from .models import All_department,Techer_info
# from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(All_department)
admin.site.register(Techer_info)

# class ViewAdmin(ImportExportModelAdmin):
#     pass
from django.contrib import admin
from routine_info.models import Routine_time,Routine_days,Room_with_na
# Register your models here.
admin.site.register(Routine_time)
admin.site.register(Routine_days)
admin.site.register(Room_with_na)

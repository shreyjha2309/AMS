from django.contrib import admin
from .models import student,subject,attendanceclass,time,attendance,NewCustomUser
# Register your models here.
admin.site.register(student)
admin.site.register(subject)
admin.site.register(time)
admin.site.register(attendance)
admin.site.register(NewCustomUser)
@admin.register(attendanceclass)
class attendaceAdmin(admin.ModelAdmin):
    list_display = ('date','status')

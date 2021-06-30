from django.contrib import admin
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    ordering = ('name', )


class SubjectAdmin(admin.ModelAdmin):
    ordering = ('name', )


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Teacher_Subject)
admin.site.register(Group)
admin.site.register(Classroom)
admin.site.register(Weekday)
admin.site.register(ScheduleStatus)
admin.site.register(Schedule)
admin.site.register(Week)
admin.site.register(Subgroup)

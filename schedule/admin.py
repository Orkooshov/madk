from django.contrib import admin
from .models import *


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'curator')
    list_editable = ('curator', )


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_editable = ('code', )


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'weekday', 'week', 'position', 'group',
                    'subject', 'teacher', 'classroom', 'status', 'subgroup')
    list_editable = ('subject', 'teacher', 'classroom', 'status', 'subgroup')


class WeekdayAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher_Subject)
admin.site.register(Group, GroupAdmin)
admin.site.register(Weekday, WeekdayAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Teacher)
admin.site.register(Classroom)

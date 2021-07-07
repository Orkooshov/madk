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

class ScheduleStatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = list_display


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher)
admin.site.register(Teacher_Subject)
admin.site.register(Group, GroupAdmin)
admin.site.register(Classroom)
admin.site.register(Weekday)
admin.site.register(ScheduleStatus, ScheduleStatusAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Week)
admin.site.register(Subgroup)

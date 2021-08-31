from django.contrib import admin
from .models import *


class GroupAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'curator')
    list_editable = ('curator', )
    prepopulated_fields = {'slug': ('name',)}


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_editable = ('code', )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('slug', 'surname', 'name', 'patronymic', 'classroom')
    list_editable = ('classroom', )
    search_fields = ('surname', 'name', 'patronymic')
    prepopulated_fields = {'slug': ('surname',)}


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('group', 'weekday', 'lesson', 'week',
                    'subgroup', 'subject', 'teacher', 'classroom', 'is_active')
    list_filter = 'group', 'weekday', 'week', 'subject', 'teacher', 'is_active'
    list_editable = 'subject', 'teacher', 'classroom', 'is_active'


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Classroom)

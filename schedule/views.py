from django.http import response
from django.http.response import HttpResponse, HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from .models import Group, Subject, Schedule, Teacher, Weekday
import datetime as dt
from .forms import TeacherForm


def index(request):
    return render(request, 'schedule/index.html')


def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'schedule/subjects.html', {'subjects': subjects})


def student(request):
    weekdays = ('Понедельник', 'Вторник', 'Среда',
                'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    weekday = weekdays[dt.datetime.now().weekday()-4]
    groups = Group.objects.all()
    return render(request, 'schedule/student.html',
                  {'weekday': weekday,
                   'groups': groups})


def teachers(request):
    teachers = Teacher.objects.order_by('name')
    return render(request, 'schedule/teachers.html', {'teachers': teachers})


def test(request):
    return HttpResponse('test')


def group(request, group_name):
    group = Group.objects.filter(name=group_name)
    if not group.exists():
        return render(request, '404.html', {'header': 'Группа не найдена', 'text': f"Группа {group_name} не существует"}, status=404)

    group = group.first()
    weekdays = Weekday.objects.all()
    group_schedules = Schedule.objects.filter(group__name=group.name)
    schedules = {}
    for weekday in weekdays:
        schedules[weekday.name] = (group_schedules.filter(
            weekday__name=weekday.name).order_by('position'))

    return render(request, 'schedule/group.html', {
        'group': group,
        'schedules': schedules,
        'weekdays': weekdays
    })

def add_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})
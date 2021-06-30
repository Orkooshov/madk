from django.shortcuts import render
from .models import Subject, Schedule, Teacher, Weekday


def index(request):
    return render(request, 'schedule/index.html')

def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'schedule/subjects.html', {'subjects': subjects})

def student(request):
    schedules = Schedule.objects.order_by('teacher')
    return render(request, 'schedule/student.html', {'schedules': schedules})

def teachers(request):
    teachers = Teacher.objects.order_by('name')
    return render(request, 'schedule/teachers.html', {'teachers': teachers})

def test(request):
    today_schedule = Schedule.objects.filter(weekday=1).order_by('position')
    return(render(request, 'schedule/test.html', {'today_schedule': today_schedule}))
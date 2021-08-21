from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from . import models as m
from django.views.generic import ListView
from .utils import get_weekday_today, get_weekday_tomorrow


def pageNotFound(request, exception):
    content = render(request, '404.html')
    return HttpResponseNotFound(content)


def index(request):
    context = {'weekday': get_weekday_today()}
    return render(request, 'schedule/index.html', context)


class SubjectListView(ListView):
    model = m.Subject
    queryset = m.Subject.objects.all()
    template_name = 'schedule/subject_list.html'
    context_object_name = 'subjects'


class TeacherListView(ListView):
    model = m.Teacher
    context_object_name = 'teachers'


class GroupListView(ListView):
    model = m.Group


def student(request):
    # todo
    groups = m.Group.objects.all()
    context = {
        'weekday_today': get_weekday_today(),
        'weekday_tomorrow': get_weekday_tomorrow(),
        'groups': groups,
    }
    return render(request, 'schedule/student.html', context)

def group(request, group_slug):
    group = get_object_or_404(m.Group, slug=group_slug)
    context = {'group': group}
    return render(request, 'schedule/group_detail.html', context)

def test(request):
    content = render(request, '404.html')
    return HttpResponseNotFound(content)

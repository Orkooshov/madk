from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from . import models as m
from django.views.generic import ListView, DetailView
from .utils import get_weekday_today, DataMixin
import datetime as dt

from rest_framework import viewsets
from .serializers import *


def pageNotFound(request, exception):
    content = render(request, '404.html')
    return HttpResponseNotFound(content)


def index(request):
    context = {'weekday': get_weekday_today()}
    return render(request, 'schedule/index.html', context)


class SubjectListView(DataMixin, ListView):
    model = m.Subject
    template_name = 'schedule/subject_list.html'
    context_object_name = 'subjects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context()
        return dict([*context.items(), *context2.items()])


class TeacherListView(DataMixin, ListView):
    model = m.Teacher
    context_object_name = 'teachers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context()
        return dict([*context.items(), *context2.items()])


class GroupListView(DataMixin, ListView):
    model = m.Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context()
        return dict([*context.items(), *context2.items()])


def teacher_detail(request, teacher_slug):
    teacher = get_object_or_404(m.Teacher, slug=teacher_slug)
    return HttpResponse(f'<h3>{teacher}</h3>')


class StudentListView(DataMixin, ListView):
    model = m.Group
    context_object_name = 'groups'
    template_name = 'schedule/student2.html'

    def get_context_data(self, **kwargs):
        context = dict([
            *super().get_context_data(**kwargs).items(),
            *self.get_user_context().items(),
            ('subgroup', m.Subgroup),
        ])
        return context


class GroupDetailView(DataMixin, DetailView):
    model = m.Group
    slug_url_kwarg = 'group_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context()
        return dict([*context.items(), *context2.items()])


def test(request):
    return render(request, '404.html')


# Rest Framework ViewSets
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = m.Subject.objects
    serializer_class = SubjectSerializer


class ClassroomViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassroomSerializer
    queryset = m.Classroom.objects


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = m.Teacher.objects
    serializer_class = TeacherSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = m.Group.objects
    serializer_class = GroupSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = m.Schedule.objects
    serializer_class = ScheduleSerializer

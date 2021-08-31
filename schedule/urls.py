from django.urls import path
from . import views as v
from madk.settings import DEBUG

urlpatterns = [
    path('', v.index, name='index'),
    path('subjects/', v.SubjectListView.as_view(), name='subject_list'),
    path('teachers/', v.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<slug:teacher_slug>/',
         v.teacher_detail, name='teacher_detail'),
    path('groups/', v.GroupListView.as_view(), name='group_list'),
    path('groups/<slug:group_slug>/',
         v.GroupDetailView.as_view(), name='group_detail'),
    path('student/', v.StudentListView.as_view(), name='student'),
    path('test/', v.test, name='test'),
] + [path('40<int:exception>/', v.pageNotFound)] if DEBUG else None

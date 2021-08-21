from django.urls import path
from . import views
from madk.settings import DEBUG

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path('groups/<slug:group_slug>/', views.group, name='group_detail'),
    path('student/', views.student, name='student'),
    path('test/', views.test, name='test'),
] +[path('40<int:exception>/', views.pageNotFound)] if DEBUG else None

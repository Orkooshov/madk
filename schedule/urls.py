from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.subjects, name='subjects'),
    path('teachers/', views.teachers, name='teachers'),
    path('student/', views.student, name='student'),
    path('test/', views.test, name='test'),
    path('student/<str:group_name>', views.group, name='group'),
    path('add_teacher', views.add_teacher, name='add_teacher')
]

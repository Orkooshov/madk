from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.subjects, name='subjects'),
    path('teachers/', views.teachers, name='teachers'),
    path('student/', views.student, name='student'),
    path('test/', views.test, name='test'),
    # path('student_today/<str:group>', views.),
]

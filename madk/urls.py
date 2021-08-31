from django.contrib import admin
from django.urls import path, include
from schedule.views import pageNotFound
from rest_framework import routers, viewsets
from schedule import views


router = routers.DefaultRouter()
router.register(r'classrooms', views.ClassroomViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register('teachers', views.TeacherViewSet)
router.register('groups', views.GroupViewSet)
router.register('schedules', views.ScheduleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schedule.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
]


handler404 = pageNotFound

from django.contrib import admin
from django.urls import path, include
from schedule.views import pageNotFound



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schedule.urls')),
]


handler404 = pageNotFound
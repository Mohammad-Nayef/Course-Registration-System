from django.urls import path
from . import views

urlpatterns = [
    path('api/courses', views.search_courses, name='search_courses'),
    path('api/registered-courses', views.register_course, name='register_course'),
    path('api/notifications', views.get_notifications, name='get_notifications'),
]

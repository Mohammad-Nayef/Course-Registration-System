from django.urls import path
from . import views

urlpatterns = [
    path('api/courses', views.search_courses, name='search_courses'),
    path('api/registered-courses', views.registered_courses, name='registered_courses'),
    path('api/notifications', views.get_notifications, name='get_notifications'),
    path('api/admin/courses', views.create_course, name='create_course'),
]

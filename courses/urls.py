from django.urls import path
from . import views

urlpatterns = [
    path('api/courses/<str:code>', views.get_course_by_code, name='get_course_details'),
    path('api/courses', views.search_courses, name='search_courses'),
    path('api/registered-courses', views.register_course, name='register_course'),
]

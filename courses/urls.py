from django.urls import path
from . import views

urlpatterns = [
    path('api/courses', views.search_courses, name='search_courses'),
    path('api/registered-courses', views.registered_courses, name='registered_courses'),
    path('api/notifications', views.get_notifications, name='get_notifications'),
    path('api/admin/courses', views.courses_for_admin, name='courses_for_admin'),
    path('api/admin/reports', views.get_reports, name='get_reports'),
    path('', views.index, name='index'),
    path('schedule', views.schedule_page, name='schedule_page'),
    path('notifications', views.notifications_page, name='notifications_page'),
    path('schedule', views.schedule_page, name='schedule_page'),
    path('statistics', views.statistics_page, name='statistics_page'),
]

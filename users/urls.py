from django.urls import path
from . import views


urlpatterns = [
    path('api/register', views.register, name='register'),
    path('register', views.register_page, name='register_page'),
    path('api/logout', views.logout, name='logout'),
    path('login/', views.login_page, name='login_page'),
    path('api/login', views.login, name='login'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('api/register', views.register, name='register'),
    path('api/login', views.login, name='login'),
    path('login', views.login_page, name='login_page'),
]

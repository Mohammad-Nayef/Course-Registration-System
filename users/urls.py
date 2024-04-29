from django.urls import path
from . import views


urlpatterns = [
    path('api/register', views.register, name='register'),
    path('register', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout', views.logout, name='logout'),
    path('', views.home_page, name='home_page'),
]

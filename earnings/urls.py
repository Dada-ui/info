from django.urls import path
from earnings import views

urlpatterns = [
    path('',views.cover,name='cover'),
    path('register',views.registerview,name='register'),
    path('login',views.loginview,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.logoutview,name='logout'),
    path('lr',views.lr,name='lr'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('add_apps/', views.add_apps, name='add_apps'),
    path('app_details/<int:pk>/', views.app_details, name='app_details'),
    path('task', views.task, name='task_detail'),
    path('points', views.points, name='points'),
]
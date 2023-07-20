"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup,name="signup"),
    path('Nlogin/', views.Nlogin, name='Nlogin'),
    path('home', views.home, name='home'),
    path('Nlogout/', views.Nlogout, name='Nlogout'),

    path('update_status/', views.update_status, name='update_status'),
   
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

    path('update_task/<int:task_id>/', views.UpdateTaskView.as_view(), name='update_task'),
    path('delete_task/<int:task_id>/', views.DeleteTaskView.as_view(), name='delete_task'),
   
    path('add_task', views.AddTaskView.as_view(), name='add_task'),
    # path('view_tasks/', views.ViewTasksView.as_view(), name='view_tasks'),
   
    # path('complete_task/<int:task_id>/', views.CompleteTaskView.as_view(), name='complete_task'),

    


]
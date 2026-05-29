"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from tasks.views import TaskCreateView, show_tasks, TaskUpdateView, TaskDelete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', TaskCreateView.as_view()),
    path('', show_tasks, name='home'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDelete, name='task_delete')
]
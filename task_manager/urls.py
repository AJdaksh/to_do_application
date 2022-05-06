"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('my_home.urls')),
    path('log_in/',include('my_home.urls')),
    path('sign_up/',include('my_home.urls')),
    path('profile/',include('my_home.urls')),
    path('add_task/',include('my_home.urls')),
    path('update/',include('my_home.urls')),
    path('delete/',include('my_home.urls')),
    path('delete/log/',include('my_home.urls')),
    path('api/tasks/',include('my_home.urls')),
    path('api/task/',include('my_home.urls')),
    path('api/task/create/',include('my_home.urls')),
    path('api/task/delete/',include('my_home.urls')),
]
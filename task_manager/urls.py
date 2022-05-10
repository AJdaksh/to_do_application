
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('my_home.urls')),
    path('log_in/',include('my_home.urls')),
    path('adminlogin/',include('my_home.urls')),
    path('logout/',include('my_home.urls')),
    path('sign_up/',include('my_home.urls')),
    path('profile/',include('my_home.urls')),
    path('adminprofile/',include('my_home.urls')),
    path('adminprofiles/',include('my_home.urls')),
    path('add_task/',include('my_home.urls')),
    path('update/',include('my_home.urls')),
    path('delete/',include('my_home.urls')),
    path('delete/log/',include('my_home.urls')),
    path('api/tasks/',include('my_home.urls')),
    path('api/task/',include('my_home.urls')),
    path('api/task/create/',include('my_home.urls')),
    path('api/task/delete/',include('my_home.urls')),
    path('filter_f/',include('my_home.urls')),
]

from django.contrib import admin
from django.urls import path
from my_home import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('log_in/',views.log_in,name='log_in'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('profile/<us_id>',views.profile,name='profile_data'),
    path('add_task/<us_id>',views.add_task,name='add_task'),
    path('update/<id>',views.update,name='update'),
    path('delete/<id>',views.delete,name='delete'),
    path('delete/log/<id>',views.delete_log,name='delete'),
    path('api/tasks',views.jsonapi,name='api_get_all'),
    path('api/task/create',views.jsonapi,name='api_create'),
    path('api/task/delete/<id>',views.jsonapi_user,name='api_delete'),
    path('api/task/<id>',views.jsonapi_user,name='api_id'),


]


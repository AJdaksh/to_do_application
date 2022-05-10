from django.contrib import admin
from .models import Task_Log,User_Detail, User_Task,Admin_Detail
# Register your models here.

@admin.register(User_Detail)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','password')

@admin.register(Admin_Detail)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','password')


@admin.register(User_Task)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','task_name','add_on_date','deadline_date','status','user_id')




@admin.register(Task_Log)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','task_name','log_title','action_date','user_id')
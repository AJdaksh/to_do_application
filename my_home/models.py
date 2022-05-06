from email.utils import format_datetime
from django.db import models

# Create your models here.


#DataBase for Users
class User_Detail(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    password=models.CharField(max_length=25)


#DataBase for Users Task
class User_Task(models.Model):
    status_choice=(('complete','Completed'),
    ('pending','Pending'))
    task_name = models.CharField(max_length=80)
    add_on_date = models.DateField(auto_now_add=True)
    deadline_date = models.DateField()
    status = models.CharField(max_length=10,choices = status_choice, default='Pending')
    user_id = models.CharField(max_length=500)




class Task_Log(models.Model):
    task_name = models.CharField(max_length=80)
    log_title = models.CharField(max_length=80)
    action_date = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=500)


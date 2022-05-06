from datetime import date,datetime
import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .serializers import User_Serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import User_Detail,User_Task,Task_Log
from .forms import Update_Task_Form, User_Add_Task_Form, User_Form,User_Login_Form,User_Task_Form,Log_Form

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


# Function for Home Page
def home(request):
    return render(request,'home.html')

# Function for LogIn Page
def log_in(request):
    if request.method == 'POST':
        login_info = User_Login_Form(request.POST)
        if login_info.is_valid():
            user_instance = login_info.save(commit=False)
            user_email = user_instance.email
            user_password = user_instance.password
            
            if User_Detail.objects.filter(email=user_email):
                userone = User_Detail.objects.filter(email=user_email)
                for i in userone:
                    user_name_in_database=i.username
                    user_password_in_database=i.password
                    user_email_in_database=i.email
                    user_id_in_database=i.id

                if user_password_in_database==user_password:
                    user_tasks = User_Task.objects.filter(user_id=user_id_in_database)
                    #return render(request,'profile.html',{'us_id':user_id_in_database ,'user_name':user_name_in_database,'user_email':user_email_in_database,'user_task':user_tasks})
                    return redirect('profile_data',us_id=user_id_in_database)
                else:
                    return redirect('http://127.0.0.1:8000/log_in/')
            else:
                return redirect('http://127.0.0.1:8000/log_in/')
        else:
            return redirect('http://127.0.0.1:8000/log_in/')
    else:
        log_in_form = User_Login_Form
        return render(request,'log_in.html',{'form':log_in_form})


# Function for SignUp Page
def sign_up(request):
    if request.method == 'POST':
        user_info = User_Form(request.POST)
        if user_info.is_valid():
            user_instance = user_info.save(commit=False)
            user_instance.username = user_instance.username + '_careers360'
            user_instance.save()
            return redirect('http://127.0.0.1:8000/log_in/')
        else:
            return redirect('http://127.0.0.1:8000/sign_up/')
    else:
        sign_up_form = User_Form
        return render(request,'sign_up.html',{'form':sign_up_form})

# Function for Profile Page
def profile(request,us_id):
    user_data = User_Detail.objects.filter(pk=us_id)
    for us in user_data:
        user_email_in_database = us.email
        user_name_in_database = us.username
        user_task = User_Task.objects.filter(user_id=us_id)
        today_date = datetime.now()
        for task in user_task:
            if (date(task.deadline_date.year,task.deadline_date.month,task.deadline_date.day) < date(today_date.year,today_date.month,today_date.day)) and task.status != 'complete':
                    task.status = 'Over'
                    task.save()
        user_tasks = User_Task.objects.filter(user_id=us_id)
        #for Log
        tasks_log = Task_Log.objects.filter(user_id = us_id).order_by('-id')
    return render(request,'profile.html',{'us_id':us_id,'user_name':user_name_in_database,'user_email':user_email_in_database,'user_task':user_tasks,'task_log':tasks_log})

# Function for Add_Task Page
def add_task(request,us_id):
    if request.method =='POST':    
        user_input_task = User_Add_Task_Form(request.POST)
        user_task= User_Task_Form()
        if user_input_task.is_valid():
            user_instance_input_task = user_input_task.save(commit=False)
            user_instance_task = user_task.save(commit=False)
            user_instance_task.task_name = user_instance_input_task.task_name
            user_instance_task.deadline_date = user_instance_input_task.deadline_date
            user_instance_task.status = 'Pending'
            user_instance_task.user_id = us_id
            user_instance_task.save()
            #for log
            task_log = Log_Form()
            task_log_ins = task_log.save(commit=False)
            task_log_ins.log_title = 'Created'
            task_log_ins.user_id = us_id
            task_log_ins.task_name = user_instance_task.task_name
            task_log_ins.save()
            user_data = User_Detail.objects.filter(pk=us_id)
            for us in user_data:
                user_id_in_database = us.id
        else:
            return HttpResponse('Wrong Input')
        return redirect('profile_data',us_id=user_id_in_database )
    else:
        add_task_form = User_Add_Task_Form
        return render(request,'add_task.html',{'form':add_task_form})


# Function for Update_Task Page
def update(request,id):
    if request.method=='POST':
        user_update_task = Update_Task_Form(request.POST)
        user_task= User_Task_Form()
        task_object= User_Task.objects.get(pk=id)
        task_user_id=task_object.user_id
        task_add_date=task_object.add_on_date
        if user_update_task.is_valid():
            user_instance_input_task = user_update_task.save(commit=False)
            user_instance_task = user_task.save(commit=False)
            user_instance_task.task_name = user_instance_input_task.task_name
            user_instance_task.deadline_date = user_instance_input_task.deadline_date
            user_instance_task.status = user_instance_input_task.status
            user_instance_task.id = id
            user_instance_task.user_id = task_user_id
            user_instance_task.add_on_date = task_add_date
            user_instance_task.save()
            #add to log
            task_log = Log_Form()
            task_log_ins = task_log.save(commit=False)
            task_log_ins.log_title = 'Updated'
            task_log_ins.user_id = task_user_id
            task_log_ins.task_name = user_instance_task.task_name
            task_log_ins.save()
        return redirect('profile_data',us_id=task_user_id)

    else:
        update_task = User_Task.objects.get(pk=id)
        update_tasks = Update_Task_Form(instance=update_task)
        return render(request,'update_task.html',{'form':update_tasks})

# Function for Delete_Task Page
def delete(request,id):
        task_object= User_Task.objects.get(pk=id)
        task_user_id=task_object.user_id
        task_object.delete()
        task_log = Log_Form()
        task_log_ins = task_log.save(commit=False)
        task_log_ins.log_title = 'Deleted'
        task_log_ins.user_id = task_user_id
        task_log_ins.task_name = task_object.task_name
        task_log_ins.save()
        return redirect('profile_data',us_id=task_user_id)


def delete_log(request,id):
        task_object= Task_Log.objects.get(pk=id)
        task_user_id=task_object.user_id
        task_object.delete()
        return redirect('profile_data',us_id=task_user_id)

#Function for getall task and create task by API
@csrf_exempt
def jsonapi(request):
    if request.method == 'GET':
        us = User_Task.objects.all()
        print(us)
        serial = User_Serializer(us, many=True)
        print(serial)
        json_data = JSONRenderer().render(serial.data)

        return JsonResponse(serial.data,safe=False)
        #return HttpResponse(json_data ,content_type = 'application/json')
    if request.method == 'POST':
        json_datas = request.body
        stream = io.BytesIO(json_datas)
        python_data = JSONParser().parse(stream)
        seriliazer = User_Serializer(data=python_data)
        if seriliazer.is_valid():
            seriliazer.save()
            res = {'msg':'created'}
            json_data1 = JSONRenderer().render(res)
            #log
            task_log = Log_Form()
            task_log_ins = task_log.save(commit=False)
            task_log_ins.log_title = 'Created through API'
            task_log_ins.user_id = python_data['user_id']
            task_log_ins.task_name = python_data['task_name']
            task_log_ins.save()
            print(python_data['user_id'])
            print(python_data['task_name'])
            return HttpResponse(json_data1,content_type='application/json')
        else:
            json_error = JSONRenderer().render(seriliazer.errors)
            return HttpResponse(json_error,content_type='application/json')



#Function for getbyid task and delete task by API
@csrf_exempt
def jsonapi_user(request,id=None):
    if request.method == 'GET':
        us = User_Task.objects.filter(user_id=id)
        serial = User_Serializer(us,many=True)
        json_data = JSONRenderer().render(serial.data)

        return JsonResponse(serial.data,safe=False)
        #return HttpResponse(json_data ,content_type = 'application/json')

    if request.method == 'DELETE':
        us = User_Task.objects.get(pk=id)
        us.delete()
        task_log = Log_Form()
        task_log_ins = task_log.save(commit=False)
        task_log_ins.log_title = 'Deleted through API'
        task_log_ins.user_id = us.user_id
        task_log_ins.task_name = us.task_name
        task_log_ins.save()
        res = {'msg':'deleted'}
        json_data1 = JSONRenderer().render(res)
        return HttpResponse(json_data1,content_type='application/json')


#changes
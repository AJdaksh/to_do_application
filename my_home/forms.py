from django import forms
from .models import  User_Detail,User_Task,Task_Log


# Form for Signup Page
class User_Form(forms.ModelForm):
    class Meta:
        model = User_Detail
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

# Form for LogIn Page
class User_Login_Form(forms.ModelForm):
    class Meta:
        model = User_Detail
        fields = ['email','password']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

# Form for Add Task Page
class User_Add_Task_Form(forms.ModelForm):
    class Meta:
        model = User_Task
        fields = ['task_name','deadline_date']
        widgets = {
            'task_name': forms.TextInput(attrs={'class':'form-control'}),
            'deadline_date':forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
        }

#Form for Update Task Page
class Update_Task_Form(forms.ModelForm):
    class Meta:
        model = User_Task
        choices=(('pending','pending'),('Complete','complete'))
        fields = ['task_name','deadline_date','status']
        status = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=choices
    )
        widgets = {
            'task_name': forms.TextInput(attrs={'class':'form-control'}),
            'deadline_date':forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
        }

#Form for User Task
class User_Task_Form(forms.ModelForm):
    class Meta:
        model = User_Task
        fields = ['task_name','deadline_date','status','user_id']
        widgets = {
            'task_name': forms.TextInput(attrs={'class':'form-control'}),
            'deadline_date':forms.DateInput(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'class':'form-control'}),
            'user_id':forms.TextInput(attrs={'class':'form-control'}),
        }



class Log_Form(forms.ModelForm):
    class Meta:
        model = Task_Log
        fields = '__all__'
        widgets = {
            'task_name': forms.TextInput(attrs={'class':'form-control'}),
            'log_title': forms.TextInput(attrs={'class':'form-control'}),
            'user_id':forms.TextInput(attrs={'class':'form-control'}),
        }


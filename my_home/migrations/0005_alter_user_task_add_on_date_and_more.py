# Generated by Django 4.0.4 on 2022-05-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_home', '0004_alter_user_task_add_on_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_task',
            name='add_on_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user_task',
            name='deadline_date',
            field=models.DateField(),
        ),
    ]

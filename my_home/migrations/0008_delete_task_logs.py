# Generated by Django 4.0.4 on 2022-05-05 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_home', '0007_task_log'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task_Logs',
        ),
    ]
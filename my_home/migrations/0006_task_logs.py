# Generated by Django 4.0.4 on 2022-05-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_home', '0005_alter_user_task_add_on_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_title', models.CharField(max_length=80)),
                ('action_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.CharField(max_length=500)),
            ],
        ),
    ]

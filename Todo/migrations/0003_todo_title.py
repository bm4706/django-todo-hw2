# Generated by Django 4.2.5 on 2023-09-07 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_todo_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default='제목!', max_length=20, verbose_name='제목'),
        ),
    ]
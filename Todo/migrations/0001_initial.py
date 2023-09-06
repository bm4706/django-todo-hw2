# Generated by Django 4.2.4 on 2023-09-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 시간!')),
            ],
        ),
    ]

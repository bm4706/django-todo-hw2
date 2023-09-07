from django.contrib import admin

from user.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)  # admin 사이트에 유저등록된걸 보여주게함

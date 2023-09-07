from django.contrib import admin

from Todo.models import Todo

# Register your models here.
admin.site.register(Todo)  # 따로 게시글을 관리하는 창

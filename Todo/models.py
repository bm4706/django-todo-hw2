from django.db import models


class Todo(models.Model):
    # user = models.ForeignKey(        "user.User", verbose_name="작성자", on_delete=models.CASCADE)
    content = models.TextField("내용")
    created_at = models.DateTimeField(
        "작성 시간", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간!", auto_now=True)


# Create your models here.

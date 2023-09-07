from django.db import models


class Todo(models.Model):
    # user = models.ForeignKey(        "user.User", verbose_name="작성자", on_delete=models.CASCADE)
    # 기본적으로 가지고있어서 그냥 추석처리
    title = models.CharField("제목", max_length=20, default="제목!")
    content = models.TextField("내용")
    created_at = models.DateTimeField(
        "작성 시간", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간!", auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.content  # admin 주소에서 todo에 작성한 글들이 content로 보여주도록


# Create your models here.

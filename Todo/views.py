from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.views.decorators.csrf import csrf_exempt


# @login_required
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()  # read
        # print(todos)
        context = {
            "todos": todos
        }
        return render(request, "todo/index.html", context)
    else:
        return HttpResponse("타당하지않은", status=405)


@csrf_exempt
def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        # user = request.user  # 현재 로그인한 사용자를 가져옵니다.

        # Todo 객체를 생성하고 데이터베이스에 저장합니다.
        Todo.objects.create(title=title, content=content, )
        # a.save()
        return redirect("/todo/index")
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse("잘못적음!")


def receive(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    return HttpResponse('작성 완료!')
# Create your views here.


def read(request, todo_id):  # db에 todo_id를 불러오려고함
    todo = Todo.objects.get(id=todo_id)
    context = {
        "todo": todo
    }
    # back_url = reverse('index')
    return render(request, "todo/detail.html", context, )

    # return HttpResponse(todo.content)


@csrf_exempt
# 삭제하기 기능
def delete(request, todo_id):
    if request.method == "POST":  # post만 가능하도록 해야함
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        # redirect를 안하고 render로 하면 주소가 점점 뒤로 쌓이게됨
        return redirect("/todo/index/")
    else:
        return HttpResponse("잘못적음!")


# 수정하기 기능
@csrf_exempt
def update(request, todo_id):
    if request.method == "POST":

        return redirect("/todo/index")
    elif request.method == "GET":
        return render(request, "todo/update.html")
    else:
        return HttpResponse("잘못적음!")

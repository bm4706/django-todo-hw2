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
@login_required(login_url="/user/login")
# django에서는 아래 굳이 안쓰고 이러한 기능을 만듬
def create(request):
    # if request.user.is_authenticated:  # 로그인 한 상태인지 여부 판별
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = request.user  # 이제 유저를 추가해줘야함

        # Todo 객체를 생성하고 데이터베이스에 저장합니다.
        Todo.objects.create(title=title, content=content, user=user)
        # a.save()
        return redirect("/todo/index")
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse("잘못적음!")
    # else:
    #     return redirect("/user/login/")


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
        todo = Todo.objects.get(id=todo_id)
        # 받아온 변경된 것들의 값을 다시 todo에 넣어주는 행위
        todo.content = request.POST["content"]
        todo.title = request.POST["title"]

        todo.save()  # 이를 db에 저장시키는 역할
        return redirect(f"/todo/read/{todo_id}/")  # 수정했으니까 다시 글로 이동해야함
    elif request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            "todo": todo
        }
        # context를 넣는 이유는 내가 수정할때 글을 확인해야해서
        return render(request, "todo/update.html", context)
    else:
        return HttpResponse("잘못적음!")

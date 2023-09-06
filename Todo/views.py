from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Todo


@login_required
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


def create(request):
    if request.method == "POST":
        Todo.objects.create(
            content=request.POST["content"], user=request.user,)
        return redirect("/todo")
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse("잘못적음!")


def receive(request):
    request.POST.get('todo')
    return HttpResponse('ok')
# Create your views here.

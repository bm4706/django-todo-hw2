from django.http import HttpResponse
from django.shortcuts import render


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
    return HttpResponse("")


# Create your views here.

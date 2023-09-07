from django.http import HttpResponse
from django.shortcuts import redirect, render

from user.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create(username=username, password=password)
        # a.save()
        return redirect("/todo/index/")
    elif request.method == "GET":
        return render(request, "user/signup.html")
    else:
        return HttpResponse("잘못적음!")

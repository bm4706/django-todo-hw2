from django.http import HttpResponse
from django.shortcuts import redirect, render

from user.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # User.objects.create(username=username, password=password)
        # user는 creat_user 써줘야함 안그러면 db를 통해 비밀번호 알아낼수있음
        User.objects.create_user(username=username, password=password)
        # a.save()
        return redirect("/todo/index/")
    elif request.method == "GET":
        return render(request, "user/signup.html")
    else:
        return HttpResponse("잘못적음!")


# 로그인 기능(장고에서 검색해서 긁어오셈)
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # username과 password를 비교해서 일치하면 로그인 성공 틀리면 none을 뱉어냄
        user = authenticate(request, username=username, password=password)
        if user is not None:  # 로그인 성공한거
            auth_login(request, user)
            # Redirect to a success page.
            return redirect("/todo/index/")
        else:
            return HttpResponse("잘못적음!")
            # Return an 'invalid login' error message.
    elif request.method == "GET":
        return render(request, "user/login.html")
    else:
        return HttpResponse("잘못적음!")


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("/todo/index/")

    else:
        return HttpResponse("잘못적음!")

import io
from django.shortcuts import render, redirect, get_object_or_404
from django_ratelimit.decorators import ratelimit
from .models import Book
from .models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseForbidden


# Create your views here.
@ratelimit(key="ip", rate="5/s", method=["POST", "GET"], block=True)
def index(request):


    user = request.user if request.user.is_authenticated else None
    books = Book.objects.all()
    return render(request, "index.html", {"books": books, "user": user})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    text_content = ""
    if book.text:
        book.text.open("rb")
        
        with io.TextIOWrapper(book.text, encoding="utf-8") as f:
            text_content = f.read()
            
    return render(request, "book_detail.html", {"book": book, "text_content": text_content, "user": request.user if request.user.is_authenticated else None})


        
def logouts(request):
    logout(request)
    return redirect("/")

@ratelimit(key="ip", rate="5/m", method=["POST"], block=True)
@login_required(login_url="login")
def users(request):
    user = request.user
    error = None
    if request.method == "POST":
        if request.POST.get("action") == "delete":
            confirmation = request.POST.get("confirmation")
            if confirmation == f"DELETE":
                
                user.delete()
                logout(request)
                return redirect("/")
            else:
                error = "Please confirm by typing 'DELETE' to delete your account."
        else:
            new_username = request.POST.get("username")
            password = request.POST.get("password")
            check = request.POST.get("check")
            avatar = request.FILES.get("avatar")

            if new_username:
                if User.objects.exclude(id=user.id).filter(username=new_username).exists():
                    return render(request, "users.html", {"user":user, "error": "this name is alredy use"})
                else:
                    user.username = new_username
            if password:
                if not check_password(check, user.password):
                    return render(request, "users.html", {"user":user, "error": "Incorrect password."})

                user.set_password(password)
            if avatar:
                user.avatar = avatar
            user.save()
            
            
            if password:
                user = authenticate(username=user.username, password=password)
                auth_login(request, user)
            return render(request, "users.html", {"user": user})
        
        
    return render(request, "users.html", {"user": user, "error": error})

@ratelimit(key="ip", rate="10/m", method=["POST", "GET"], block=True)
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
        
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username alredy used"})
        
        
        if confirmation != password:
            return render(request, "register.html", {"error": "passworpasswords do not match"})
        
        hashed_password = make_password(password)

        new_user = User(username=username, password=hashed_password)
        new_user.save()
        

        auth_login(request, new_user)        
        # request.session["user_id"] = new_user.id
        response = redirect("index")
        response.set_cookie("auth", "true", max_age=3600000, secure=True)
        return response
    
    return render(request, "register.html")

@ratelimit(key="ip", rate="10/m", method=["POST", "GET"], block=True)
def login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = User.objects.filter(username=username).first()
            
        if  user and check_password(password, user.password):
            auth_login(request, user)
            # request.session["user_id"] = user.id
            response = redirect("index")
            response.set_cookie("auth", "true", max_age=36000000, secure=True)
            return response

        else:
            return render(request, "login.html", {"error": "Not corect username or password"})
        

    return render(request, "login.html")
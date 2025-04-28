from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from .models import Books
from .models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
# Create your views here.
@ratelimit(key="ip", rate="5/s", method=["POST", "GET"], block=True)
def index(request):

    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id) if user_id else None
    books = Books.objects.all()
    return render(request, "index.html", {"books": books, "user": user})
    
    
@ratelimit(key="ip", rate="10/m", method=["POST", "GET"], block=True)
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username alredy used"})
        
        hashed_password = make_password(password)

        new_user = User(username=username, password=hashed_password)
        new_user.save()
        return redirect("login")
    
    return render(request, "register.html")

@ratelimit(key="ip", rate="10/m", method=["POST", "GET"], block=True)
def login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.filter(username=username).first()
            
            if check_password(password, user.password):
                auth_login(request, user)
                request.session["user_id"] = user.id
                return redirect("index")

            else:
                return render(request, "login.html", {"error": "Not corect username or password"})
        
        except User.DoesNotExist:
                return render(request, "login.html", {"error": "not corect username or password"})
    return render(request, "login.html")
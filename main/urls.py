from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("users/", views.users, name="user"),
    path("logout/", views.logouts, name="logout"),
    path("book/<int:pk>/", views.book_detail, name="book_detail")
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

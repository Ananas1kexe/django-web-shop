from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("book/<int:pk>/", views.book_detail, name="book_detail"),
    path('book/<int:pk>/like/', views.like_book, name='like_book'),
    path("report/<int:book_id>/", views.report, name="report"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logouts, name="logout"),
    path("setting/", views.setting, name="user"),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

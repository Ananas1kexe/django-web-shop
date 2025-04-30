from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class BlockedUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/admin/login/') or request.path.startswith("/logout") or request.path.startswith("/users"):
                return None

        user = getattr(request, "user", None)
        if (user and user.is_authenticated and user.blok and not user.is_superuser):
            return HttpResponse("Your account is blocked Logout <a href='/logout'>LogOut</a> <a href='/users'> Delete</a>")
        return None
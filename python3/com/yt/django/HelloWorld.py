from django.http import HttpResponse
from python3.com.yt.django.entity.User import User, Role


def hello(request):
    user = User(1234)
    role = Role(1, "张三")
    role.id
    role.name
    return HttpResponse(user.name)

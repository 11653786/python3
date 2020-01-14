from django.http import HttpResponse
#引入models模块就行了
from python3 import models


def hello(request):
    models.User.objects.create(name="张三", age=18, sex=1, salary=114)
    return HttpResponse("12345")

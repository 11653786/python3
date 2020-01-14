from django.http import HttpResponse

# 引入models模块就行了
from python3 import models


def hello(request):
    # 保存方法1
    # models.User.objects.create(name="张三", age=18, sex=1, salary=114)
    # 保存方法2
    user = models.User(name="张三", age=19, sex=1, salary=114)
    user.save()
    return HttpResponse("12345")


def update(request):
    user = "{name:zhangsan,age:11,sex:2,salary:113}"
    models.User.objects.filter(id=1).update(name='修改')
    return HttpResponse("update")

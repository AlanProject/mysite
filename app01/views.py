from django.shortcuts import render
from app01 import models
# Create your views here.
def index(request):
    return render(request,'index.html',)
def regist(request):
    return render(request,'regist.html',)
def login(request):
    return render(request,'login.html',)
def test(request):
    l = models.Users.objects.get(name="alan")
    t = l.name
    return render(request,'test.html',{'passwd':t},)
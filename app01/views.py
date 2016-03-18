#coding:utf8
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

from app01 import models
# Create your views here.
def index(request):
    return render(request,'index.html',)
def regist(request):
    return render(request,'regist.html',)
def login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        if username == 'alan' and password == 'admin':
            request.session['username'] = username
            return redirect('/app01/home/')
        else:
            return render(request,'login.html',{'status':'usererror'})
    else:
        return render(request,'login.html',)


def home(request):
    username = request.session.get('username')
    return render(request,'home.html',{'username':username})


# def test(request):
#     l = models.Users.objects.get(name="alan")
#     t = l.name
#     return render(request,'test.html',{'passwd':t},)


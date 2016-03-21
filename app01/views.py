#coding:utf8
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

from app01 import models
from forms import UserInfo
# Create your views here.
def index(request):

    return render(request,'index.html',)
def regist(request):
    if request.method == 'POST':
        form = UserInfo(request.POST)
        if form.is_valid():
            data = form.clean()
            name = data.get('name')
            pwd = data.get('passwd')
            c = data.get('user_choice')
            print data
            return HttpResponse(c)
    return render(request,'regist.html',{'form':UserInfo,})

# 登陆处理函数
def login(request):
    # 如果页面请求状态为POST
    if request.method == 'POST':
        # 获取页面中提交的信息
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        # 判断用户名密码是否正确
        if username == 'alan' and password == '123':
            # 如果正确则设置session的login状态为True
            request.session['login'] = True
            # 并跳转到home页面
            return redirect('/app01/home/')
        # 如果用户名密码不匹配则还跳转回登陆页面
        else:
            return render(request, 'login.html')
    # 如果请求状态不为POST则跳转回login页面
    else:
        return render(request, 'login.html')

# home处理函数
def home(request):
    # 获取session的login标签为防止login无状态设定默认值为False
    session = request.session.get('login', False)
    # 如果session为True 则跳转到home页
    if session:
        return render(request, 'home.html')
    # 如果session为False则跳转到登陆页
    else:
        return redirect('/app01/login/')

# 退出处理函数
def logout(request):
    # 删除session的login标识
    del request.session['login']
    # 跳转到登陆界面
    return redirect('/app01/login/')


# def test(request):
#     l = models.Users.objects.get(name="alan")
#     t = l.name
#     return render(request,'test.html',{'passwd':t},)


#!/usr/bin/env python
#-*- coding:utf-8 -*-
import shutil
import os
import time
# 设置全局变量
soucrce = 'xiangshou.war'
project = 'xiangshou'
www_dir = '/data/www'
tomcat_dir = '/usr/local/tomcat'
# 输出相关选择信息
print '='*18+'Tuling manger'+'='*18
print '''1.Tomcat Restart
2.Deployment Projects
3.Exit'''
print '='*50

#开始执行

try:
    change = raw_input('Please enter the operation you want to do "1" or "2" >>> ')
    if int(change) == 1:
        # 关闭服务
        os.system('sh %s/bin/shutdown.sh' % (tomcat_dir))
        print 'Tomcat server is shutdown ok !'
        # 启动服务
        os.system('sh %s/bin/startup.sh' % (tomcat_dir))
        print 'Tomcat server is startup ok !'
    elif int(change) == 2:
        t = time.strftime('%Y%m%d%H')
        # 备份旧的war包
        shutil.move('%s/webapps/%s.war'% (tomcat_dir,project,),'%s/webapps/%s.war.%s.bak'% (tomcat_dir,project,t))
        #将新的war包部署到webapps目录下
        shutil.move('%s/%s'%(www_dir,project),'%s/webapps/%s.war'% (tomcat_dir,project))
        # 重启tomcat部署业务
        os.system('sh %s/bin/shutdown.sh' % (tomcat_dir))
        print 'Tomcat server is shutdown ok !'
        os.system('sh %s/bin/startup.sh' % (tomcat_dir))
        print 'Tomcat server is startup ok !'
        # 将项目从webapps软链到/data/www
        os.system('ln -s %s/webapps/%s %s' % (tomcat_dir,project,www_dir))
        print 'Setup OK'
    else:
        pass
except ValueError as e:
    print 'You entered is not a numeric type. Please try again.'

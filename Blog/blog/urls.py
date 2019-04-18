"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.shortcuts import render
# def index(request):
#     print(request)
#     #return  HttpResponse('hello django!')
#     #return JsonResponse({'user':'fdfdsfdfs'}) #数据返回
#     ''' 请求进来了 我组成数据返回给客户端'''
#     d={}
#     # d['method']=request.method
#     # d['path'] = request.path
#     # d['path_info'] = request.path_info
#     # d['GETparams'] = request.GET
#     d=zip(('abcdef'),[1,2,3,4])
#
#     #return JsonResponse(d)
#     return  render(request,'index.html',{'result':d,'content':'hellow'})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', index),
    # url(r'^index$', index),#路由配置
    url(r'^user/', include("user.urls")) , # 路由配置 用户模块
    url(r'^post/', include("post.urls"))  # 路由配置  博文模块
]

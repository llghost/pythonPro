from django.conf.urls import url,include
from .views import  reg,login,test

urlpatterns = [
    url(r'^reg$', reg), # 路由配置 注册
    url(r'^login$', login) , # 路由配置 登陆
    url(r'^test$', test)  # 路由配置  认证是否过期
]

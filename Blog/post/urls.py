from django.conf.urls import url,include
from .views import  pub,get,getall

urlpatterns = [
    url(r'^pub$', pub), # 路由配置 发布
    url(r'^(\d+)$', get) , # 路由配置  查/post/10 会给get(request，id) 多传入一个 参数
     url(r'^$', getall)  # 路由配置  查所有 认证是否过期
]

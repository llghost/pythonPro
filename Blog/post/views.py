from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse,HttpResponseBadRequest
from user.views import authration
from user.models import User
from .models import Post, Content
import simplejson
import datetime
import  math


# Create your views here.


@authration  # 验证登陆的装饰器
def pub(request: HttpRequest):
    post = Post()
    content = Content()
    try:
        # 1.新增博文 及内容
        playload = simplejson.loads(request.body)
        title = playload['title']
        post.title = title
        post.postdate = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        post.author = User(id=request.user.id)  # 注入id post 表中只要id
        post.save()
        contents = playload['content']
        content.post = post
        content.content = contents
        content.save()
        return JsonResponse({"post_id": post.id})
    except Exception as e:
         return HttpResponseBadRequest()  # 如果出现异常返回实例


def get(request: HttpRequest, id):
    print(id)
    post = Post.objects.filter(pk=id).get()
    res = {
        'title': post.title,
        'postdate': post.postdate.timestamp(),
        'author': post.author.name,
        'content':post.content.content
    }
    return JsonResponse({"post": res})

def validate(d:dict,name,type_fun,default,validate_fun):
    try:
       ret= type_fun(d.get(name,1))
       ret=validate_fun(ret,default)

    except:
        ret=1
    return ret;

def getall(request: HttpRequest):  #post?page=1&size=10
    # try:
    #    page= int(request.GET.get('page',1))
    # except:
    #     page=1
    page=validate(request.GET,"page",int,1,lambda x,y : x if x >0  else y)
    # try:
    #     size = int(request.GET.get('size', 20))
    # except:
    #     size = 1
    size=validate(request.GET,"size",int,10,lambda x,y : x if x >0 and x<101  else y)
    start=(page-1)*size  #1-1*20  2-1*20
    qs=Post.objects
    count=qs.count()

    posts = qs.order_by('-id')[start:start+size]

    print(posts.query)
    res = {"posts": [
        {"postid": post.id, "title": post.title} for post in posts
    ],
    "pagination":{
        "page":page,#当前页
        "size":size,#每页条数
        "count":count,#总条数
        "pages":math.ceil(count/size)#总页数
    }
    }
    return JsonResponse(res)

from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse,HttpResponseBadRequest
import simplejson
import logging
logging.basicConfig(level=logging.INFO)
from .models import User
from django.conf import  settings
import  jwt
import datetime
import bcrypt
# Create your views here.
key=settings.SECRET_KEY
EXP_TIME=60*60*8  #登陆过期时间 30秒
#加密 返回签过名的 tonken
def get_token(user_id):
    return jwt.encode(
        {'user_id':user_id,
         'exp':int(datetime.datetime.now().timestamp())+EXP_TIME},#增加时间戳 判断是否哦重发token 或者重新登录    增加过期时间 pyjwt 内部自动验证
        key,'HS256')\
        .decode()

def reg(request:HttpRequest):
    # print(request)
    # print(type(request))
    # print(request.GET)
    # print(request.POST)
    try:
        playload = simplejson.loads(request.body)
        email = playload['email']
        query=User.objects.filter(email=email) #objects 对象 django 提供的管理器 专门用于查询 类型未Manager
        #query = User.objects.filter(pk__lt=1)  # objects 对象 django 提供的管理器 专门用于查询 类型未Manager
        print(query)
        print(type(query),query.query)
        if query:
            return HttpResponseBadRequest("已存在")
        else:
            print("-"*30)
        name = playload['name']
        password = playload['password']
        # bcrypt 加密 通过加盐  就是增加前后缀 和 增加穷举的时间  来防止暴力破解  $2b$ 算法
        en_pwd=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        print(name,email,password,en_pwd)
        user=User()
        user.email=email
        user.name=name
        user.password=en_pwd
        try:
            user.save()
            #return JsonResponse({'user_id':user.id})  #返回插入成功的id  隐含帮你查了
            return JsonResponse({'token':get_token(user.id)})  # 返回t签过名的oken给客户端
        except Exception as e:
            raise
        #raise 1#手动抛出异常 except 捕获后会返回一个异常实例 400

    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest() #如果出现异常返回实例

def login(request:HttpRequest):
    print(request.body)
    login_info=simplejson.loads(request.body)
    email=login_info['email']
    password=login_info['password']
    print(email,password)
    user=User.objects.filter(email=email).get()#根据邮箱获取用户
    print(user)

    if bcrypt.checkpw(password.encode(),user.password.encode()):#验证密码
           token=get_token(user.id)
           ret=JsonResponse({
             "name":user.name,
             "email":user.email,
             "password":user.password,
               "token":token
           })
           ret.set_cookie('JWT',token)
           return  ret
    else:
        return HttpResponseBadRequest("不存在")

def authration(view):
    def _raper(request:HttpRequest):
        try:
            #自定义header jwt
            print(list(request.META.keys()))
            #play_load=request.META.get('HTTP_COOKIE')#
            play_load = request.META.get('HTTP_JWT')  #
            print(play_load,"pppppppppppppppppppppppppppppppppppppppppp")

            # print(play_load.split("=")[1],"---------------------------")
            # playload=play_load.split("=")[1]
            if not play_load:#如果没拿到 表示没有登陆过
                return HttpResponse(status=401)
            try:
              play_load=jwt.decode(play_load,settings.SECRET_KEY,algorithms=['HS256'])#框架内部自动验证是否过期
              print(play_load,"+++++++++++++++++++++++++++++++++")
            except Exception as e:
                print(e, "---------------------------")
                return HttpResponse(status=401)
            userid=play_load.get("user_id",-1)
            user=User.objects.filter(pk=userid).get()
            request.user=user
            print("*"*30)
        except Exception as e:
            logging.info(e)
            return HttpResponseBadRequest('')
        return view(request)

    return  _raper

@authration  #需要用户登录过才能继续的操作
def test(request:HttpRequest):
    return HttpResponse('TEST')
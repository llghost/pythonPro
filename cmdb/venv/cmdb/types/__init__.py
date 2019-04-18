import importlib
import ipaddress
#反射 动态获取类型实例
instance_cache={}
classes_cache={}

def get_instance(type: str, **options):

    p,c=type.rsplit('.',maxsplit=1)
    print(p,c)
    mod=importlib.import_module(p)#导入模块
    cls=getattr(mod,c)

    key= ",".join("{}={}".format(k,v )for k,v in sorted(options.items()))
    print(key)
    key="{}|{}".format(type,key)
    print(key)
    obj=instance_cache.get("key")
    if obj:
        return obj

    obj=cls(**options)
    instance_cache[key]=obj
    if isinstance(obj,BaseType):
        return obj
    raise TypeError("Type error No subclass is BaseType.{}".format(type))

class BaseType:
    def __init__(self,**options):
        self.__dict__["options"]=options

    def __getattr__(self, item):
         return self.options.get(item)

    def stringfiy(self,value):
        raise  NotImplementedError

    def descfiy(self):
        raise  NotImplementedError

class Int(BaseType):
    def stringfiy(self,value):
        print(self.max)
        if(value>self.max):
            raise ValueError("too big")
        if(value<self.min):
            raise ValueError("too small")
        return  str(int(value))

    def descfiy(self,value):
        return  value

class IP(BaseType):
    def stringfiy(self,value):
        val=ipaddress.ip_address(value)
        print("fffffffffff",str(val))
        if not str(val).startswith(self.prefix):
            raise ValueError("not a standard IP")
        return str(val)

    def descfiy(self,value):
        return  value

# def init_class_cache():
#     print("------------------init--------------------")
#     print(globals())
#     mod=globals().get("__package__")
#     print(mod)
#     for k,v in globals().items():
#
#         if type(v)==type and k !='BaseType' and issubclass(v,BaseType):
#             classes_cache[k]=v
#             #classes_cache['.'.join((mod,k))]=v
#             print(classes_cache)
#             #print(k, type(v))
#     print("------------------init end --------------------")

def inject_classes_cache():
    mod = globals().get('__package__')

    for k,v in globals().items():
        if type(v) == type and k != 'BaseType' and issubclass(v, BaseType):
            classes_cache[k] = v
            classes_cache[".".join((__name__, k))] = v
            print(classes_cache)

inject_classes_cache()

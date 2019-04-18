# class A:
#     def __new__(cls,*args,**kwargs):
#         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         print(1,cls)
#         print(2,args)
#         print(3,kwargs)
#         if not hasattr(cls,'_instance'):
#             setattr(cls,'_instance',super().__new__(cls))
#             setattr(cls,'_count',0)
#         return cls._instance
#
#     def __init__(self,url,debug):
#         print("init------------------------")
#         print(5,self._count)
#         if self._count==0:
#             self.url=url
#             self.debug=debug
#             self.__class__._count=1
#         else:
#             raise Exception('JUST ONE INSTANCE')
#
#     def __repr__(self):
#        return  "<B {} {} >".format(self.url,self.debug)
#
# b=A(1,debug=2)
# print(4,b.__dict__)
# import time
# time.sleep(2)
# b1=A(10,20)
# print(b1.__dict__)

#单例
import functools

def signleton(cls):
    instance=None

    @functools.wraps(cls)
    def warper(*args,**kwargs):
        print(args)
        print(kwargs)
        nonlocal instance
        if not instance:
            instance=cls(*args,**kwargs)
        return  instance
    return warper

# @signleton
# class B:
#     ''' B class'''
#     def __init__(self,url,debug):
#         self.url=url
#         self.debug=debug
# c=B("1",True)
#
# print(id(c),c.__dict__,c.__doc__)
# d=B("2",False)
# print(id(d),d.__dict__)
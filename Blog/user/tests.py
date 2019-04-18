from django.test import TestCase

# Create your tests here.
import  jwt

key='select'
playload={'playload':'abc123'}
token=jwt.encode(playload,key,'HS256') #加密 返回一个b
print(token)
print(jwt.decode(token,key,algorithms=['HS256']))
header,playload,signature=token.split(b'.') #tokem 分为3部分（key，负载数据，签名）用 . 断开
print(header)
print(playload)
print(signature)

import base64
def addeq(b:bytes):
    rem=len(b)%4
    return b+b'='*rem

print('header',base64.urlsafe_b64decode(addeq(header)))
print('playload',base64.urlsafe_b64decode(addeq(playload)))
print('signature',base64.urlsafe_b64decode(addeq(signature)))
from urllib import  request,response
from urllib.request import Request,urlopen
import  random
from urllib import parse
# response=request.urlopen("http://www.baidu.com")
# print(response.closed)
# with response:
#     print(1,type(response))
#     print(2,response.status,response.reason)#状态
#     print(3,response.geturl()) #返回连接
#     print(4,response.info()) #头 headers
#     print(5,response.read())#内容  返回byte
#     print(5, response._method)  # 方法
#
# print(response.closed)

# url='https://movie.douban.com/'
# ua_list = [
#      "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/57.0.2987.133 Safari/537.36",# chrome
# "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/537.36 (KHTML, like Gecko)Version/5.0.1 Safari/537.36", # safafi
# "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", # Firefox
# "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)" # IE
# ]
# ua =random.choice(ua_list)
# request=Request(url)
# request.add_header('User-Agent',ua)
# print(type(request))
#
# response=urlopen(request,timeout=20)
# print(type(response))
# with response:
#     print(2,response.status,response.getcode(),response.reason)#状态
#     print(3,response.geturl()) #返回连接
#     print(4,response.info()) #头 headers
#     print(5,response.read())#内容
#
# print(6,request.get_header('User-agent'))
# print(7,'user-agent'.capitalize())

u=parse.urlencode({'url':'http://www.magedu.com/python',
'p_url':'http://www.magedu.com/python?id=1&name=张三',})
print(u)

u=parse.urlencode({'wd':'中',}) #编码
url='https://www.baidu.com?{}'.format(u)
print(url)
print('中'.encode('utf-8'))
print(parse.unquote(u))#解码
print(parse.unquote(url))
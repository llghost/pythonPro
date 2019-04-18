# from urllib import parse
# from urllib import request,response
# from urllib.request import  Request,urlopen
# keyword=input(">>>>>>>>>>>>>>input a word to search")
# data=parse.urlencode({"q":keyword})
# base_url = 'http://cn.bing.com/search'
# url="{}?{}".format(base_url,data)
# print(url)
#
# ua = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36 Maxthon/5.2.6.1000"
#
# request=Request(url,headers={"User-agent":ua})
# response  =urlopen(request)
# with response:
#     with open("d:/search.html",'wb') as f:
#         f.write(response.read())



##########################################get##################################
# from urllib.request import Request, urlopen
# from urllib.parse import urlencode
# keyword = input('>> 请输入搜索关键字 ')
# data = urlencode({
# 'q':keyword
# })
# #https://www.baidu.com/s?w=%E4%B8%AD
# base_url = 'http://cn.bing.com/search'
# url = '{}?{}'.format(base_url, data)
# print(url)
# # 伪装
# ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
# request = Request(url, headers={'User-agent':ua})
# response = urlopen(request)
# with response:
#    with open('d:/bing.html', 'wb') as f:
#       f.write(response.read())


#print('成功')
##########################################post##################################
from urllib.request import Request, urlopen
from urllib.parse import urlencode
#import simplejson

data = urlencode({'name':'张三,@=/&*', 'age':'6'})
#https://www.baidu.com/s?w=%E4%B8%AD
url = 'http://httpbin.org/post'
print(url)
# 伪装
ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
request = Request(url, headers={'User-agent':ua},data=data.encode()) #post 请求  data 必须传bytes
response = urlopen(request)
with response :
      text=response.read()
     # s=simplejson.loads(text)
      print(text)
print('成功')
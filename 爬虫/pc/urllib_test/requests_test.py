import  requests

ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
url = 'https://movie.douban.com/'
response=requests.request('GET',url,headers={"User-agent":ua})
with response as res:
    print(res.status_code)
    print(res.url)
    print(res.request.url)
    print(response.text[:100])
    print(1,res.request.headers)
    print(2,res.headers)




# 直接使用Session
import requests
ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
urls = ['https://www.baidu.com/s?wd=magedu', 'https://www.baidu.com/s?wd=magedu']
session = requests.Session()

with session:
   for url in urls:
        print("---------------------------")
        response = session.get(url, headers={'User-Agent':ua})
        with response:
            print(type(response))
            print(response.url)
            print(response.status_code)
            print(response.request.headers) # 请求头
            print(response.cookies) # 响应的cookie
            print(response.text[:20]) # HTML的内容
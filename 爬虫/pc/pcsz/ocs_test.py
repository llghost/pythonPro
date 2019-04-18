import requests
from bs4 import BeautifulSoup

url = "https://my.oschina.net/"

headers = {
    'Host': "my.oschina.net",
    'Connection': "keep-alive",
    'Cache-Control': "max-age=0",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'Referer': "https://www.oschina.net/home/login?goto_page=https%3A%2F%2Fmy.oschina.net%2Fu%2F4114756",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Cookie': "_user_behavior_=c73f716c-991c-416a-93da-7260b7e2a64c; _reg_key_=wybaqsycSX1mSxl0IceI; aliyungf_tc=AQAAAOYJ/S+9TgkAXgw2dOiKRh2S95dt; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1555063688,1555064115; oscid=oyxkbViBs16SgeHA3ddBuD1q8hVSsx9yuGFUdWDDgEFa9Twu4b9Vs74%2B4l6ulcuSQfVvKtCz9HxhqMFZeoRwN89Q2BRX2IaP4oNJ7f4fo5BdzKbQafB6zptQfLH5Rm2WZVmUBrC8S4AVz7fG9Hvh%2BSYYM%2BVqXY8L; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1555064133"
    }

response = requests.request("GET", url, headers=headers)
with response as res:
    txt=res.text
    soup=BeautifulSoup(txt,'lxml')
    info=soup.find(class_="user-info")
    print(info.get_text(strip=True))
    # with open("d:/oschina.html","w",encoding='utf-8') as f:
    #      f.write(response.text)
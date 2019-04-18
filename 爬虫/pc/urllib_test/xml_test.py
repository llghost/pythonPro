import  requests
from lxml import  etree

ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
url = 'https://movie.douban.com/'
response=requests.request('GET',url,headers={"User-agent":ua})
with response as res:
    # print(res.status_code)
    # print(res.url)
    # print(res.request.url)
    # print(response.text[:100])
    # print(1,res.request.headers)
    # print(2,res.headers)
    html=etree.HTML(response.text)
    titles=html.xpath("//div[@class='billboard-bd']//tr/td/a/text()") # 返回文本列表//div[@class='billboard-bd']//tr/td/a/text()") # 返回文本列表")
    for t in titles:
        print(t)
from concurrent.futures import  ThreadPoolExecutor
import requests
from  queue import  Queue
from bs4 import BeautifulSoup
import  threading
import logging
import time

logging.basicConfig(level=logging.INFO)

#http://www.xubiaozhaopinwang.com/tools/submit_ajax.ashx?action=m_job_list&page=1&page_size=8&_keyword=_&_order=4&_jobtype=0&_area=_&_jobproperty=0&_date=0&_workyears=0&_sex=0&_degree=0
#https://news.cnblogs.com/n/page/5/
# Base_url='https://news.cnblogs.com'
# PARAM='/n/page/'

Base_url='http://www.xubiaozhaopinwang.com/tools/submit_ajax.ashx?action=m_job_list'
PARAM='/n/page/'
headers = {
'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)Maxthon/5.0 Chrome/55.0.2883.75 Safari/537.36",
}

urls=Queue()
htmls=Queue()
outputs=Queue()
event=threading.Event()
#创建url
def create_urls(start,stop,step=1):
    for i in range(start,stop+1,step):
        urls.put("{}{}{}/".format(Base_url,PARAM,i))
    print("url 创建完毕")

#爬取页面线程函数
def crawel():
    while not event.is_set():
        try:
            url=urls.get(True,1)
            with requests.get(url,headers=headers) as res:
               html=res.text
               htmls.put(html)
               print(html)
               print(url)
        except Exception as e:
            logging.error(e)
#解析
def parser():
    while not event.is_set():
        try:
            html=htmls.get(True,1)
            soup=BeautifulSoup(html,'lxml')
            titles=soup.select('h2.news_entry a')
            for title in titles:
               print(title," -----------parser-----------")
               val=title.text,Base_url+title.get('href')
               outputs.put(val)
               print(val)
        except Exception as e:
            logging.error(e)

def save(path):
    with open(path,'a+',encoding='utf-8') as f:
        while not event.is_set():
            try:
                text,url=outputs.get(True,1)
                print(text,url,"---------------------------")
                f.write('text:{},url:{}\n'.format(text,url))
                f.flush()
            except Exception as e:
                logging.error(e)

executor=ThreadPoolExecutor(10)
executor.submit(create_urls,1,10) #异步创建10个url 放入待爬取队列
executor.submit(parser) #异步创建 解析线程
executor.submit(save,"d:/blog.log")#异步创建 存储线程
for i in range(7):
    executor.submit(crawel)#7个爬取线程



while True:
    inp=input(">>>>>")
    if inp.strip()=="q":
        event.set()
        print("quit")
        time.sleep()
        break
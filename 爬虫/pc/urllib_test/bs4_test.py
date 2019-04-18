from  bs4 import BeautifulSoup
import  re

#四种对象
#BeautifulSoup将HTML文档解析成复杂的树型结构，每个节点都是Python的对象，可分为4种：
#BeautifulSoup、Tag、NavigableString、Comment
with open('test.html',encoding='utf-8') as f:
    soup=BeautifulSoup(f,"lxml")
    # print(type(soup))
    # print(soup.builder) #解析器
    # # print(soup.prettify()) #格式打印
    # print("-"*30)
    # print(soup.div,type(soup.div))#type  Tag
    print(soup.find_all())
    print(soup.find_all('p',attrs={"id":'first'}))
    print(soup.find_all(['p','img'],id=True))
    print(list(map(lambda  x:x.name,soup.find_all())))
    print(2,soup.find_all(text=re.compile('\w+')))
    print(3,soup.find_all(id=re.compile('\w+')))

    def class_filter(tag):
        return len(tag.attrs.get('class',[])) >1

    print(soup.find_all(class_filter))  #传方法

    print(soup.select('p#first'))
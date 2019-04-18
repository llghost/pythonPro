from selenium import  webdriver  #核心对象
from selenium.webdriver.support.ui import Select #操作下拉框的类
import datetime
import  time
import  random

driver=webdriver.PhantomJS(r'D:\BaiduNetdiskDownload\马哥2018 python全能工程师网络班资料(2)\slides\python21-爬虫\install\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.set_window_size(1280,2400)

url = "http://cn.bing.com/search?q=%E9%A9%AC%E5%93%A5%E6%95%99%E8%82%B2"
#driver.get(url)

def savepic():
    base_dir="d:/"
    filename="{}{:%Y%m%d%H%M%S}{:03}.png".format(base_dir,datetime.datetime.now(),random.randint(1,100))
    driver.save_screenshot(filename)


# savepic()#刚访问就截图，ajax 数据未返回所以是空白的
# time.sleep(5) #等待ajax 返回并渲染数据 再次截图就能看到结果
# savepic()
# MAX_WAIT=5
# for i in range(MAX_WAIT):
#     time.sleep(1)
#     try:
#        ele=driver.find_element_by_id("b_content") #如果找不到说明没有ajax 还没有返回数据
#        print(ele)
#        savepic()
#     except Exception as e:
#         print(e)


#select 下拉框操作
# url = "https://www.oschina.net/search?scope=project&q=python"
# driver.get(url)
# ele=driver.find_element_by_name('tag1') #通过便前面查找元素
# print(ele.tag_name)#input
# print(ele.get_attribute("value"))
# print(driver.current_url)
# savepic()
# s=Select(ele)  #针对 select 标签 其他不适用
# s.select_by_index(1)
# print(driver.current_url)
# savepic()

#模拟登陆
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
url='https://www.oschina.net/home/login'
driver.implicitly_wait(2)  #隐式等待  全局设置

driver.get(url)

savepic()

userMail=driver.find_element_by_id("userMail")
userMail.send_keys("17366923916")
userPassword=driver.find_element_by_id("userPassword")
userPassword.send_keys("llsocoll12")
savepic()
userPassword.send_keys(Keys.ENTER) #模拟回车
#time.sleep(3)
print(driver.current_url,"fffffffffffffffff")
savepic()
#显示等待
ele=WebDriverWait(driver,1).until(
    ec.presence_of_element_located((By.CLASS_NAME,"current-user-avatar"))
)
userinfo=driver.find_element_by_class_name("current-user-avatar")
print(userinfo.get_attribute('title'))
print(driver.get_cookies())
# while True:
#     time.sleep(1)
#     print(driver.current_url)
#     try:
#         userinfo=driver.find_element_by_class_name("user-info")
#         print(userinfo.text)
#         savepic()
#         break
#     except Exception as e:
#         print(e)
#
#
#
# cookie=driver.get_cookies()
# print(cookie)
driver.close()
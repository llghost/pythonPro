# import scrapy
# from scrapy.http.response.html import HtmlResponse
#
# response=HtmlResponse('d:/douban.txt',encoding="utf-8")
#
# with open("d:/douban.txt",encoding='utf-8') as f:
#     response._set_body(f.read())
#    # print(response.text)
#
#     # subjects=response.xpath("//li[@class='subject-item']").extract()
#     # for sub in subjects:
#     #     print(sub.xpath('.//h2/a/text()').extract())
#     print("-------------------------xpath 选择----------------------")
#     subjects = response.xpath('//li[@class="subject-item"]')
#     for subject in subjects:
#         title = subject.xpath('.//h2/a/text()').extract()  # list
#         print(title[0].strip())
#         rate = subject.xpath('.//span[@class="rating_nums"]/text()').extract()  # list
#         print(rate[0].strip())
#
#     print("-------------------------选择器选择----------------------")
#     subjects = response.css('li.subject-item')
#     for subject in subjects:
#         title = subject.css('h2 a::text').extract()  # list
#         print(title[0].strip())
#         rate = subject.css('span.rating_nums::text').extract()  # list
#         print(rate[0].strip())
#
#     print("-------------------------混合使用----------------------")
#     subjects = response.css('li.subject-item')
#     for subject in subjects:
#         href = subject.xpath('//h2').css('a::attr(href)').extract()  # list
#         print(href[0].strip())
#         rate = subject.xpath('.//span[@class="rating_nums"]/text()').re(r'^9.*')  # list
#         if rate:
#             print(rate[0].strip())


import  redis

db=redis.Redis('192.168.1.113')
db.set("testbin",0b01100010)
print(db.get("testbin"))
print(db.keys("*"))
db.incrby('s4',4)
print(db.get('s4'))
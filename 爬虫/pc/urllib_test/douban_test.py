from urllib import request,response
from urllib.request import Request,urlopen
from  urllib import parse
import simplejson

url='https://movie.douban.com/j/search_subjects'
data=parse.urlencode({
'type':'movie',
'tag':'热门',
'page_limit':10,
'page_start':10
})
url="{}?{}".format(url,data)
print(parse.unquote(url))
ua='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36'
request=Request(url,data=data.encode(),headers={'User-agent':ua})

with urlopen(request) as res:
    subjects=simplejson.dumps(res.read())
    print(len(subjects))
    print(subjects)









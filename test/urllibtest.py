from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request('http://www.thsrc.com.tw/tw/TimeTable/SearchResult')
postData = parse.urlencode([
    ("StartStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation", "9c5ac6ca-ec89-48f8-aab0-41b738cb1814"),
    ("DepartueSearchDate", "2019/01/10"),
    ("DepartueSearchTime", "06:00"),
    ("DepartueTrainCode", "")
])
req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
resp = urlopen(req, data=postData.encode('utf-8'))

print(resp.read().decode("utf-8"))






# 案例一
# from urllib import request
# from urllib import parse
#
# req = request.Request('http://www.baidu.com')
# req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
# resp = request.urlopen(req)
# resp = request.urlopen(req)
# print(resp.read().decode("utf-8"))

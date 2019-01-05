import urllib.request as urllib2

from http import cookiejar

url = "http://www.baidu.com"

print ('第一种方法')
response1 = urllib2.urlopen(url)
print (response1.getcode())
print (len(response1.read()))

print ('第二种方法')
resquest = urllib2.Request(url)
resquest.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(resquest)
print (response2.getcode())
print (len(response2.read()))

print ('第三种方法')
cj = cookiejar.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print (response3.getcode())
print (cj)
print (len(response3.read()))

import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'world':'hello'}), encoding='utf-8')   #urlencode用来将一个字典类型的数据转化成一个get请求

request = urllib.request.Request('http://python.org') #构建请求

response = urllib.request.urlopen('http://httpbin.org/post', data=data)

response_python = urllib.request.urlopen(request)

print(response.status)  #状态码
#print(response.getheaders())    #响应头
#print(response.getheader('Date'))

print(response_python.read().decode())
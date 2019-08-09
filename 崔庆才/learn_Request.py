import requests
import time

# start = time.time()

s = requests.Session()

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
    #其他请求头信息都可以忽略，但是cookie这个选项一定要保留，这个维持登录会话的关键！
'Cookie': '_ga=GA1.2.744310192.1555558746; MoodleSession=4tshuul1kdtbreiir18lcsps50; MOODLEID1_=%251C%25DB%250B%2518%25D6%2560%25D3%257B',
'Host': 'aie.skyconcord.com',
'Referer': 'http://aie.skyconcord.com/login/index.php',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

data = {
'id': '32',
'mode': 'overview',
'sesskey': '9YlzdciDGd',
'_qf__quiz_overview_settings_form': '1',
'mform_isexpanded_id_preferencespage': '1',
'mform_isexpanded_id_preferencesuser': '1',
'attempts': 'enrolled_with',
'stateinprogress': '0',
'stateinprogress': '1',
'stateoverdue': '0',
'stateoverdue': '1',
'statefinished': '0',
'statefinished': '1',
'stateabandoned': '0',
'stateabandoned': '1',
'onlygraded': '0',
'onlyregraded': '0',
'pagesize': '30',
'slotmarks': '1',
'submitbutton': '显示报告'
}

response = s.post('http://aie.skyconcord.com/mod/quiz/report.php',headers=headers,data=data)    #hearders是请求头信息，data是form data也就是post的表单信息，这些信息都可以在浏览器的network的加载过程后显示


print(type(response))

print(response.status_code)
# print(type(response.text))    #返回内容是字符串类型的数据，无需decode
print(response.text)          #返回内容
print(response.cookies)
# print(response.content)   #打印二进制流，用于保存图片音频和视频文件

# end = time.time()
# t = end - start
# print(t)

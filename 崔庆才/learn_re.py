import re #对字符串操作的逻辑公式

################################################################
###re.match从头开始匹配，如果开头没有匹配上就算了，后面是什么都不管了###
################################################################

a = 'Hello 123 4567 World_This is a Regex Demo'

# print(len(a))
# print(re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo$',a).span()) #match用来判断是否获得匹配，如果有则返回re.Match object,否则返回none

b = 'Hello 1234567 World_This is a Regex Demo'

# result = re.match('^Hello\s(\d+)\sWorld.*Demo$',b)  #用小括号扩住的内容是一个group，用result.group(序号)的形式来查询这些group
# print(result)
# print(result.groups())  #查询定义的第一个group内的内容

#贪婪匹配
# greedy = re.match('^Hello.*(\d+).*Demo$',b)
# print(greedy)
# print(greedy.group(1))      #返回值为7而不是1234567，因为前面的123456被.*贪婪地匹配掉了，只剩余了一个7
#
# #非贪婪匹配
# non_greedy = re.match('^Hello.*?(\d+).*Demo$',b)    #在.*之后添加一个问号'？'意为非贪婪匹配，也就是说当.*？匹配到后面的数字\d+时就不再将数字内容算作.*的内容了
# print(non_greedy)
# print(non_greedy.group(1))

#匹配模式   因为含有换行符，.*无法匹配换行符 解决办法：在match方法里传入第三个参数re.S
content = "Hello 1234567 World_This \nis a Regex Demo"
result1 = re.match('^He.*?(\d+).*Demo$',content)
result2 = re.match('^He.*?(\d+).*Demo$',content,re.S)
print(result1)
print(result2.group(1))

################################################################
###re.search会扫描整个字符串，并返回第一个成功的匹配##################
################################################################
print(re.match('123',content))
print(re.search('123',content))

################################################################
###re.findall从头开始匹配，查询符合条件的所有结果，返回值为一个列表#####
################################################################

################################################################
###re.sub用来替换字符串，第一个参数是原字符串，第二个参数是要替换的字符串，第三个参数是整条长字符串
################################################################
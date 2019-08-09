from pyquery import PyQuery as pq #pq是一个css选择器，遵循其选择语法的规则

html = '''
        <div>
            <ul>
                <li class="item-0">first item</li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                <li class-"item-0"><a href="link5.html">fifth item</a></li>
            </ul>
        </div>
'''

doc = pq(html)      #pq的第一种初始化方式 将一段html代码声明为一个pq的实例
print(doc('li'))

url = pq(url='http://www.google.com')    #pq的第2种初始化方式 URL初始化，将url作为参数输入，或者输入一个本地的html文件也可以
print(url('title').text())

print(doc('div').find('li')) #pq是一个类，它的find方法返回值也是一个类，所以可以套用迭代来不断查找子元素。find查找所有子元素
print(doc('div').children('li'))    #children用来查找直接子元素，传入的参数是一个css选择器。但一般是用find方法，比较方便

#查找父元素，用parent方法，查找祖先节点用parents，这些方法通常都可以接受一个参数，用以接受css选择器
print(type(doc('list').parent()))
print((doc('list').parent()))

#兄弟元素用siblings方法
#doc().siblings()

#元素的遍历：针对多个元素 pyquery的items方法生成一个generator迭代器，可以用for循环遍历其中的元素，每一个元素都是一个pyquery的类

##获取信息
#获取属性 方法和Jquery一样 都是attr方法
print('###')
a = doc('.item-0.active a')
print(a)
print(a.attr('href'))
print(a.attr.href)      #两种方式均可

#获取文本 text方法
#获取html html方法

##DOM操作 -- 节点操作
#addClass  removeClass
#attr css
# remove -- 实用方法
html = '''
    <div class='wrap'>
        Hello World
        <p>This is a paragraph.</p>
    </div>
    '''
###由于这里的div里嵌套的Hello文本以下还嵌套了一个<p>标签，所有当需要选取Hello World的时候会取到<p>内的文本：This is a paragraph.所以需要用remove方法做删除
print("####")
doc = pq(html)
wrap = doc(".wrap")
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())

####伪类选择器 css3
li = doc("li:nth-child(2)")

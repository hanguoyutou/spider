from bs4 import BeautifulSoup

####
#bs4有4中解析器，包括python标准解析器：html.parser,lxml HTML解析器：lxml,XML解析器：xml,和html5lib解析器：html5lib
#这里只讲解lxml解析器

html = '''
        "<html>\n",
      " <head>\n",
      "  <title>\n",
      "   The Dormouse's story\n",
      "  </title>\n",
      " </head>\n",
      " <body>\n",
      "  <p class=\"title\" name=\"dromouse\">\n",
      "   <b>\n",
      "    The Dormouse's story\n",
      "   </b>\n",
      "  </p>\n",
      "  <p class=\"story\">\n",
      "   Once upon a time there were three little sisters; and their names were\n",
      "   <a class=\"sister\" href=\"http://example.com/elsie\" id=\"link1\">\n",
      "    <!-- Elsie -->\n",
      "   </a>\n",
      "   ,\n",
      "   <a class=\"sister\" href=\"http://example.com/lacie\" id=\"link2\">\n",
      "    Lacie\n",
      "   </a>\n",
      "   and\n",
      "   <a class=\"sister\" href=\"http://example.com/tillie\" id=\"link3\">\n",
      "    Tillie\n",
      "   </a>\n",
      "   ;\n",
      "and they lived at the bottom of a well.\n",
      "  </p>\n",
      "  <p class=\"story\">\n",
      "   ...\n",
      "  </p>\n",
      " </body>\n",
      "</html>\n",
      "The Dormouse's story\n"
      '''
s = html.split("\"")
html = ''
for i in s:
    html += i

s = html.split("\n")
html = ''
for i in s:
    html += i

s = html.split(",")
html = ''
for i in s:
    html += i

soup = BeautifulSoup(html, 'lxml')

# print(soup.title)
# print(soup.head)
# print(soup.p.attrs['name']) #打印属性信息，attrs可以省略
# print(soup.p.b.string) #通过多个点好表示嵌套关系类似xpath,string用来显示标签内的内容（不含tag）
#
# print(soup.p.contents)  #contents用来显示子节点信息，返回值为list类型
# print(soup.html.children)   #类似contents，不过它返回的是一个迭代器，而非列表，可以透过enumerate和for循环将序号和内容打印,这类似re库里的findall和finditer
# for i,child in enumerate(soup.html.children):
#     print(i,child)
#
# print(soup.html.descendants)    #类似children用法，也是返回迭代器，但是它不光返回子节点，而且还返回孙子节点

# #父节点和祖先节点
# print(soup.a.parent)    #父节点
# for i,p in enumerate(soup.a.parents):   #祖先节点 返回迭代器
#     print(i,p)
#
# #兄弟节点的获取，也就是并列节点
# print(list(enumerate(soup.a.next_siblings)))    #打印后面的兄弟节点
# print(list(enumerate(soup.a.previous_siblings)))    #打印之前的兄弟节点
#
# #以上为标签选择器，特点是快捷，但有时不能满足解析需求，比如选择id为XX或者class为XX的标签时，则需要一些标准选择器api来处理。
# #find_all
# soup.find_all('ul')
# #find_all还可以搭配attrs使用键值对的形式查找指定属性的元素
# soup.find_all(attrs={'id':'list-1'})    #未找到内容就返回空，同样的attrs可以被省略，同时将键值对改为=等号的形式
# #当要查找每类标签时，class是python的内置关键字，所以要在后面加一个下划线用以区别class_
# soup.find_all(class_='element')
# #要查找文本内容时，使用text属性
# soup.find_all(text='Foo')   #查找出现Foo的标签的内容
# #find返回单个元素，findall是返回所以匹配结果
# soup.find('ul')

#bs提供css选择器
html = '''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bay</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
            '''

soup = BeautifulSoup(html,'lxml')

# print(soup.select(('.panel .panel-heading')))   #class用.表示
# print(soup.select('ul li'))                     #标签拿来直接用
# print(soup.select('#list-2 .element'))          #id用#表示
# print(type(soup.select('ul')[0]))               #返回值是一个bs4.element.Tag，说明它也可以使用嵌套迭代选择元素

#用中括号获取属性，也可以加attrs
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

#获取内容,使用get_text方法
for li in soup.select('li'):
    print(li.get_text())

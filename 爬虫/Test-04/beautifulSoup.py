from bs4 import BeautifulSoup
'''
beautifulSoup “美味的汤，绿色的浓汤”

一个灵活又方便的网页解析库，处理高效，支持多种解析器。
利用它就不用编写正则表达式也能方便的实现网页信息的抓取

##基本使用

标签选择器

在快速使用中我们添加如下代码：
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)

通过这种soup.标签名 我们就可以获得这个标签的内容
这里有个问题需要注意，通过这种方式获取标签，如果文档中有多个这样的标签，返回的结果是第一个标签的内容，如上面我们通过soup.p获取p标签，而文档中有多个p标签，但是只返回了第一个p标签内容

获取名称

当我们通过soup.title.name的时候就可以获得该title标签的名称，即title

获取属性

print(soup.p.attrs['name'])
print(soup.p['name'])
上面两种方式都可以获取p标签的name属性值

获取内容

print(soup.p.string)
结果就可以获取第一个p标签的内容：
The Dormouse's story

嵌套选择

我们直接可以通过下面嵌套的方式获取

print(soup.head.title.string)

子节点和子孙节点
'''

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
'''soup=BeautifulSoup(html)
print(soup.prettify())
print('=========')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p["class"])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link3'))
for link in soup.find_all('a'):
    print(link.get('href'))
    print(link.get('id'))
'''
html1 = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
#soup=BeautifulSoup(html1)
#print(soup.prettify())
#for link in soup.find_all('a'):
 #   string1=link.get(soup.span.string)
  #  href=link.get('href')
   # print(string1,href)
#print(soup.p.contents)
'''通过下面的方式也可以获取p标签下的所有子节点内容和通过contents获取的结果是一样的，
但是不同的地方是soup.p.children是一个迭代对象，而不是列表，只能通过循环的方式获取素有的信息
'''
#print(soup.p.children)
#for i,child in enumerate(soup.p.children):
   # print(i,child)

'''
## 父节点和祖先节点 

## 通过soup.a.parent就可以获取父节点的信息

通过list(enumerate(soup.a.parents))可以获取祖先节点，这个方法返回的结果是一个列表，会分别将a标签的父节点的信息存放到列表中，以及父节点的父节点也放到列表中，并且最后还会讲整个文档放到列表中，所有列表的最后一个元素以及倒数第二个元素都是存的整个文档的信息

## 兄弟节点

soup.a.next_siblings 获取后面的兄弟节点
soup.a.previous_siblings 获取前面的兄弟节点
soup.a.next_sibling 获取下一个兄弟标签
souo.a.previous_sinbling 获取上一个兄弟标签
'''

'''
## 标准选择器
find_all

find_all(name,attrs,recursive,text,**kwargs)
可以根据标签名，属性，内容查找文档'''

html2='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
'''soup=BeautifulSoup(html2)
print(soup.prettify())
print(soup.find_all('ul'))#find_all获取HTML中ul标签
print('==================')
print(soup.find_all('ul')[0])
print(type(soup.find_all('ul')[0]))
print('===================')
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
print('===================')
#attrs可以传入字典的方式来查找标签，但是这里有个特殊的就是class,因为class在python中是特殊的字段，
# 所以如果想要查找class相关的可以更改attrs={'class_':'element'}或者soup.find_all('',{"class":"element})，
# 特殊的标签属性可以不写attrs，例如id
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
print('===================')
#查到的所有的text='Foo'的文本
print(soup.find_all(text='Bar'))
for A in soup.find_all(text='Bar'):
    print(A)
'''
## find

## find(name,attrs,recursive,text,**kwargs)
## find返回的匹配结果的第一个元素
'''其他一些类似的用法：
find_parents()返回所有祖先节点，find_parent()返回直接父节点。
find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点
'''
'''
##CSS选择器

通过select()直接传入CSS选择器就可以完成选择
熟悉前端的人对CSS可能更加了解，其实用法也是一样的
.表示class #表示id
标签1，标签2 找到所有的标签1和标签2
标签1 标签2 找到标签1内部的所有的标签2
[attr] 可以通过这种方法找到具有某个属性的所有标签
[atrr=value] 例子[target=_blank]表示查找所有target=_blank的标签
'''
'''
#print(soup.select('.panel .panel-heading'))
#print(soup.select('ul li'))
#print(soup.select('#list-2 .element'))
#print(type(soup.select('ul')[0]))
'''
## 获取内容

## 通过get_text()就可以获取文本内容
'''
for li in soup.select('li'):
    print(li.get_text())
    #print('------')
    print(li.get_text()[0])
'''
## 获取属性
## 或者属性的时候可以通过[属性名]或者attrs[属性名]
'''
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
'''
html3='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

'''
NavigableString类来包装Tag中的字符串一个NavigableString字符串与python中的Unicode字符串相同，##通过unicode()方法可以直接将
NavigableString对象转换成Unicode字符串：
unicode_string=unicode(soup.p.string)
'''
'''
soup=BeautifulSoup(html3,'html5lib')
print(soup.select("div div class"))
print(soup.select(".element"))
print(soup.div.attrs)
print(soup.div['class'])
print(soup.div.get('class'))
div1=soup.find(class_='panel-body')
ul1=div1.find(class_='list')
li_string=ul1.find_all('li')
for string1 in li_string:
    string_text=string1.string

    print(string_text)
    print(type(string_text))'''

'''
##子节点
Tga中的.contents和.children是非常重要的，Tag的.contents属性可以将Tag子节点以列表的方式输出
字符串是没有.contents属性
#print(soup.div.contents)
.children属性返回的是一个生成器，可以对Tag的子节点进行循环
#for child in soup.div.children:
    print(child)
##.string
##.strings属性主要应用于tag中包含多个字符串的情况，可以进行循环遍历
##.stringed_strings属性可以去掉输出字符串包含的空格或空行
repr()方法
'''

import re
import requests

'''\w      匹配字母数字及下划线
\W      匹配f非字母数字下划线
\s      匹配任意空白字符，等价于[\t\n\r\f]
\S      匹配任意非空字符
\d      匹配任意数字
\D      匹配任意非数字
\A      匹配字符串开始
\Z      匹配字符串结束，如果存在换行，只匹配换行前的结束字符串
\z      匹配字符串结束
\G      匹配最后匹配完成的位置
\n      匹配一个换行符
\t      匹配一个制表符
^       匹配字符串的开头
$       匹配字符串的末尾
.       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[....]  用来表示一组字符，单独列出：[amk]匹配a,m或k
[^...]  不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
*       匹配0个或多个的表达式
+       匹配1个或者多个的表达式
?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
{n}     精确匹配n前面的表示
{m,m}   匹配n到m次由前面的正则表达式定义片段，贪婪模式
a|b     匹配a或者b
()      匹配括号内的表达式，也表示一个组

         函数　　 	            描述
compile(pattern) 	创建模式对象
search(pattern,string) 	在字符串中寻找模式
match(pattern,string)　　 	在字符串开始处匹配模式
split(pattern,string) 	根据模式分割字符串
findall(pattern,string) 	列表形式返回匹配项
sub(pat,repl,string) 	pat匹配想用repl替换
escape(string) 	特殊字符转义

方法一:re.match()
尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None
语法格式：
re.match(pattern,string,flags=0)

result.group()获取匹配的结果
result.span()获去匹配字符串的长度范围

#这里需要说一下的是通过re.group()获得结果后，如果正则表达式中有括号，则re.group(1)获取的就是第一个括号中匹配的结果
#尽量使用泛匹配，使用括号得到匹配目标，尽量使用非贪婪模式，有换行符就用re.S
强调re.match是从字符串的起始位置匹配一个模式

方法二：re.search
re.search扫描整个字符串返回第一个成功匹配的结果

方法三：re.findall
搜索字符串，以列表的形式返回全部能匹配的子串

方法四：re.sub
替换字符串中每一个匹配的子串后返回替换后的字符串
re.sub(正则表达式，替换成的字符串，原字符串)

方法五：re.compile
将正则表达式编译成正则表达式对象，方便复用该正则表达式

content="hello 123 4567 World_This is a regex Demo"
result=re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
print(result.group())
print(result)
print(result.span())

print('------------------------------------')
content="hello 123 4567 World_This is a regex Demo"
result=re.match("^h.*o$",content)
print(result.group())
print(result.span())
print(result)

print('------------------------------------')
contents="hello 123456 World_This is a regex Demo"
results=re.match('^hello\s(\d+)\s*Demo$',contents)
print(results)
#print(result.group())
#print(result.group(1))
#print(result.span())

content="hello 1234567 World_This is a regex Demo"
result=re.match('^he.*?(\d+).*Demo',content)
print(result)
print(result.group(1))
print('-------------------------------------')

content="""hello 123456 word_this
my name is zhaofan
"""
result=re.match('he.*?(\d+).*?zhaofan$',content,re.S)
print(result)
print(result.group(1))
print('------')
content='price is $5.00'
result=re.match('price is \$5\.00',content)
print(result)
print(result.group())'''
html =''' <div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
'''result=re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print(result.groups())
print(result.group(1))
print(result.group(2))
#result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
#print(result)
#print(result.groups())
#print(result.group(1))
#print(result.group(2))
result=re.search('li.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print(result.groups())
print(result.group(1))
print(result.group(2))

print('----------------')
result=re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print(type(result))
for results in result:
    print(results)
    print(results[0],results[1],results[2])
print('===========================================')
content="Extra things hello 12355 Word_this is a regex Demo extra things"
content=re.sub('\d+','',content)
print(content)
content=re.sub('\s+','',content)
print(content)
'''
######################################################
'''url="http://book.douban.com/"
content=requests.get(url).text
#print(content)
pattern=re.compile('li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results=re.findall(pattern,content)
print(requests)
for result in results:
    url,name,author,date=result
    author=re.sub('\s','',author)
    date=re.sub('\s','',date)
    print(url,name,author,date)
'''
pat=re.compile('A')   #m=re.search('A','CBA')
print(pat)
m=pat.search('CBA')
print(m)
m=pat.search('CND')
print(m)
m=re.match('a','acb')
print(m)

result=re.findall('a','ASDaDFGAa')
print(result)
print(result[0])
for results in result:
    print(result)
result=  re.sub('a','A','aSBacd')
print(result)
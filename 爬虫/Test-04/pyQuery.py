#!/usr/bin/python
# -*- coding: utf-8 -*-
html = '''
<html>
<head>
 <title>this is title</title>
</head>
<body>
 <p id="hi">Hello, World</p>
 <p id="hi2">Nihao</p>
 <div class="class1">
  <img src="1.jpg" />
 </div>
 <ul>
  <li>list1</li>
  <li>list2</li>
 </ul>
</body>
</html>
'''

'''print
d('title')  # 相当于css选择器，根据html标签获取元素
print
d('title').text()  # text()方法获取当前选中的文本块

print
d('#hi').text()  # 相当于id选择器，直接根据id名获取元素
print
d('p').filter('#hi2').text()  # 可以根据id或class得到指定元素
print
d('.class1')  # 相当于class选择器
print
d('.class1').html()  # html()方法获取当前选中的html块
print
d('.class1').find('img').attr('src')  # 查找嵌套元素，并选中属性
print
d('ul').find('li').eq(0).text()  # 根据索引号获取多个相同html元素中的某一个
print
d('ul').children()  # 获取所有子元素
print
d('ul').children().eq(0)  # 根据索引获取子元素
print
d('img').parents()  # 获取父元素
print
d('#hi').next()  # 获取下一个元素
print
d('#hi').nextAll()  # 获取后面全部元素块
print
d('p').not_('#hi2')  # 返回不匹配选择器的元素
# 遍历所有匹配的元素
for i in d.items('li'):
    print
    i.text()
print[i.text()
for i in d.items('li')]  # 遍历用于列表推倒
print
#d.make_links_absolute(base_url='http://www.baidu.com')   把html文档中的相对路径变为绝对路径
'''
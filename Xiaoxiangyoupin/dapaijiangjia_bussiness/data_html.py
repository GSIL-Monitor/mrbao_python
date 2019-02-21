# coding:utf-8
import codecs


def write_html(html_name: str, twoCategoryId, goods_list):
    '''
    :param html_name: 保存的HTML名
    :param twoCategoryId: 二级分类名
    :param goods_list: 商品list
    :return: 
    '''
    title = {'categoryOneName': '一级类目',
             'categoryTwoName': '二级类目',
             'brandName': '名牌名',
             'title': '标题',
             'img': '商品图片',
             'goodsCode': '商品code',
             'goodSource': '商品来源',
             'price': '商品价格',
             'markDownRange': '商品降价幅度'
             }
    html_data = codecs.open('%s.html' % html_name ,'w', encoding='utf-8')
    html_data.write('<html>')
    html_data.write("<head><meta charset='utf-8'/></head>")
    html_data.write("<body>")
    html_data.write("<h1>%s<h1>" % twoCategoryId)

    html_data.write("<table class='table table-striped'>")
    html_data.write("<thead>")
    html_data.write("<tr>")
    html_data.write("<th>%s</th>" % title['categoryOneName'])
    html_data.write("<th>%s</th>" % title['categoryTwoName'])
    html_data.write("<th>%s</th>" % title['brandName'])
    html_data.write("<th>%s</th>" % title['title'])
    html_data.write("<th>%s</th>" % title['img'])
    html_data.write("<th>%s</th>" % title['goodsCode'])
    html_data.write("<th>%s</th>" % title['goodSource'])
    html_data.write("<th>%s</th>" % title['price'])
    html_data.write("<th>%s</th>" % title['markDownRange'])
    html_data.write("</tr>")
    html_data.write("</thead>")
    html_data.write("<tbody>")
    for data in goods_list:
        html_data.write("<tr>")
        html_data.write("<td>%s</td>" % data['categoryOneName'])  # 一级类目
        html_data.write("<td>%s</td>" % data['categoryTwoName'])  # 二级类目
        html_data.write("<td>%s</td>" % data['brandName'])  # 名牌名
        html_data.write("<td>%s</td>" % data['title'])  # 标题
        html_data.write("<td><a href=%s>img</a></td>" % data['img'])
        html_data.write("<td>%s</td>" % data['goodsCode'])  # 商品code
        html_data.write("<td>%s</td>" % data['goodSource'])  # 商品来源
        html_data.write("<td>%s</td>" % data['price'])  # 商品价格
        html_data.write("<td>%s</td>" % data['markDownRange'])  # 商品降价幅度
        html_data.write("</tr>")
    html_data.write("</tbody>")
    html_data.write("</table>")
    html_data.write("</body>")
    html_data.write("</html>")
    html_data.close()

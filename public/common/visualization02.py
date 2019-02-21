# -*- coding: UTF-8 -*-
import time
from pyecharts import Bar,Gauge
from pyecharts import Pie,Style,Grid

#bar=Bar('Interface test results','Here is the subtitle')

#bar.add('Interface',['Login','Shiming','mensuo','fangyuan'],[10,11,21,33])

#bar.show_config()

#bar.render()

'''
add参数

label_pos='center'标签的位置
is_label_show=True 标签是否展示
label_text_color='' 标签文字的颜色
legend_top="center"图例位置

'''
path='E:\\Python_study\\PYREQUESTS\\report\\visualization_report\\'
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = path + now +'-'+ 'visualization.html'

def data_visualization(login_success_value=0,login_failure_value=0,shiming_success_value=0,shiming_failure_value=0,fangyuan_success_value=0,fangyuan_failure_value=0
                       ,mensuo_success_value=0,mensuo_failure_value=0):
    '''
    数据可视化,连环拼图
    :param login_success_value: 
    :param login_failure_value: 
    :param shiming_success_value: 
    :param shiming_failure_value: 
    :param fangyuan_success_value: 
    :param fangyuan_failure_value: 
    :param mensuo_success_value: 
    :param mensuo_failure_value: 
    :return: 
    '''

    pie = Pie('Results of each interface test', 'Data to Jenkins', title_pos='center')
    style = Style()
    pie_style = style.add(label_pos="center",
                          is_label_show=True,
                          label_text_color='#6E6E6E')

    pie.add('', ['Login Success', 'Login Failure'], [login_success_value, login_failure_value], center=[10, 30], radius=[20, 30],
            **pie_style)

    pie.add('', ['ShiMing Success', 'ShiMing Failure'], [shiming_success_value, shiming_failure_value], center=[10, 80], radius=[20, 30],
            **pie_style)

    pie.add('', ['FangYuan Suceess', 'FangYuan Failure'], [fangyuan_success_value, fangyuan_failure_value], center=[40, 30], radius=[20, 30], **pie_style)

    pie.add('', ['MenSuo Success', 'MenSuo Failure'], [mensuo_success_value, mensuo_failure_value], center=[40, 80], radius=[20, 30], legend_top="center",
            **pie_style)

    pie.show_config()
    pie.render(filename)

def bar_graph(attr,v1,v2):
    '''柱状图'''
    bar=Bar('Out of house analysis results','Data to Jenkins',title_pos='left')
    attr=attr
    v1=v1
    v2=v2
    bar.add('Lock',attr,v1,is_stack=True)
    bar.add('No Lock',attr,v2,is_stack=True)
    bar.show_config()
    bar.render(filename)

'''
add(name, attr, value,
    scale_range=None,
    angle_range=None, **kwargs)
    
    name -> str
    图例名称
    attr -> list
    属性名称
    value -> list
    属性所对应的值
    scale_range -> list
    仪表盘数据范围。默认为 [0, 100]
    angle_range -> list
    仪表盘角度范围。默认为 [225, -45]

'''
def dashboard():
    '''仪表盘'''
    gauge=Gauge('Results of each interface test')
    style=Style()
    gauge_style=style.add(
        label_pos='center',
        is_label_show=True,
        label_text_color=None)

    gauge.add('Login Interface Test','Rate of passing',70,**gauge_style)

    #gauge.add('FangYuan Interface Test','Rate of passing',60,**gauge_style)
    gauge.show_config()
    gauge.render(filename)

def gird():
    '''
    混合图表
    
    1引入 Grid 类，from pyecharts import Grid
    2实例化 Grid 类，grid = Grid() ，可指定 page_title, width, height, jhost 参数。
    3使用 add() 向 grid 中添加图，至少需要设置一个 grid_top, grid_bottom, grid_left, grid_right 四个参数中的一个。grid_width 和 grid_height 一般不用设置，默认即可。
    4使用 render() 渲染生成 .html 文件
    
    add(chart,
    grid_width=None,
    grid_height=None,
    grid_top=None,
    grid_bottom=None,
    grid_left=None,
    grid_right=None)
    
    chart -> chart instance
    图表实例
    grid_width -> str/int
    grid 组件的宽度。默认自适应。
    grid_height -> str/int
    grid 组件的高度。默认自适应。
    grid_top -> str/int
    grid 组件离容器顶部的距离。默认为 None, 有'top', 'center', 'middle'可选，也可以为百分数或者整数
    grid_bottom -> str/int
    grid 组件离容器底部的距离。默认为 None, 有'top', 'center', 'middle'可选，也可以为百分数或者整数
    grid_left -> str/int
    grid 组件离容器左侧的距离。默认为 None, 有'left', 'center', 'right'可选，也可以为百分数或者整数
    grid_right -> str/int
    grid 组件离容器右侧的距离。默认为 None, 有'left', 'center', 'right'可选，也可以为百分数或者整数
    '''

    bar = Bar('Results of each interface test', 'Data to Jenkins',height=720)
    attr = ['Login', 'ShiMing', 'FangYuan', 'MenSuo']
    v1 = [20, 23, 22, 44]
    v2 = [12, 2, 4, 6]
    bar.add('Test Success', attr, v1, is_stack=True)
    bar.add('Test Failure', attr, v2, is_stack=True)

    gauge = Gauge('Results of each interface test', title_color='#4F4F4F', title_top='50%')

    gauge.add('Login Interface Test', 'Use case completion rate', 70, abel_text_color='#6E6E6E')

    grid=Grid()
    grid.add(bar,grid_bottom='60%')
    grid.add(gauge,grid_top='60%')
    grid.render(filename)

if __name__ == '__main__':
    #data_visualization(40,60)
    #bar_graph()
    #dashboard()
    gird()

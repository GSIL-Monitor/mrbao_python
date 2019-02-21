# coding:utf-8
import requests
import codecs
import re
from Xiaoxiangyoupin.xiaoxiang_module.xiaoxiang_dapiajiangjia import DapaiJiangJia
from data_html import write_html


def dapiajiangjia(category):
    '''
    :param category: 
    :return: 
    '''
    dpai = DapaiJiangJia()
    data_List = []
    global twoCategoryName
    global twoCategoryId
    '''
    # 手机数码 category=1
    # 箱包 category=2
    # 美妆 category=3
    # 女鞋 category=4
    # 男鞋 category=5
    # 男装 category=6
    # 女装 category=7
    '''

    result_oneCategoryList = dpai.queryAllOneCategory()  # 查询所有一级类目
    oneCategoryList = result_oneCategoryList['body']['oneCategoryList']  # 获取一级类目
    print(oneCategoryList)
    if oneCategoryList != None:  # 判断一级类目列表是否为空
        for result_oneCategoryList in oneCategoryList:
            category_list = result_oneCategoryList['categoryOneId']  # 获取categoryOneId放入category_list中
            if category == category_list:  # 判断category是否等于传入值并且是否在
                result_queryPageByOneId = dpai.queryPageByOneId(
                    oneCategoryId=category)  # 根据一级类目找二级类目，再根据二级类目找品牌
                twoCategoryList = result_queryPageByOneId['body']['twoCategory']  # 获取二级类目以及二级类目下的的品牌列表
                for result_twoCategoryList in twoCategoryList:
                    # print(result_twoCategoryList)
                    if result_twoCategoryList not in data_List:
                        data_List.append(result_twoCategoryList)
                    else:
                        print('result_twoCategoryList为NULL')

        return data_List
    else:
        print('oneCategoryList为NULL')


def huoqu_shangping(*args):
    '''
    :return: 
    '''
    dpai = DapaiJiangJia()

    for result_data in args[0]:
        twoCategoryId = result_data['twoCategoryId']  # 获取二级类目id
        twoCategoryName = result_data['twoCategoryName']  # 获取二级类目名称
        brands = result_data['brands']  # 获取品牌列表
        for reslut_brands in brands:
            if reslut_brands != None:
                brandId = reslut_brands['brandId']
                response_data = dpai.queryGoods(brandId=brandId, barId=twoCategoryId)
                print("正在请求商品id为%s二级分类为%s的商品" % (brandId, twoCategoryName))
                if 'goods' in response_data['body'].keys():
                    good_list = response_data['body']['goods']
                    try:
                        twoCategoryName = re.sub('\/', '', twoCategoryName)
                        reslut_brands['brandName']=re.sub('\/', '',reslut_brands['brandName'])
                        html_name = twoCategoryName + "--" + reslut_brands['brandName']
                        write_html(html_name=html_name, twoCategoryId=twoCategoryName, goods_list=good_list)  # 写入HTML
                    except:
                        raise print("write_html出错")
                else:
                    print('goods 不存在')


if __name__ == '__main__':
    for i in range(1,8):
        a = dapiajiangjia(category=i)
        huoqu_shangping(a)
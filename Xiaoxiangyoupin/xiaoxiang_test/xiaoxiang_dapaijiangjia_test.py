# -*- coding: UTF-8 -*-
import unittest
import pytest
from Xiaoxiangyoupin.xiaoxiang_module.xiaoxiang_dapiajiangjia import DapaiJiangJia
from Xiaoxiangyoupin.xiaoxiang_common.startEnd import StartEnd


class Test_api_dapaijiangjia(StartEnd, DapaiJiangJia):
    '''移动端大牌降价'''

    def test_recommendPage01(self):
        '''首页推荐top4 分类下的top3品牌的top1商品oneCategoryList，twoCategoryListGoodsTop4反回字段不为空'''
        print("执行test_recommendPage01")
        response = self.recommendPage()
        self.assertEqual(response['heads']['code'], 200)
        try:
            self.assertIsNotNone(response['body']['oneCategoryList'])  # 一级类目列表
            self.assertEqual(len(response['body']['oneCategoryList']), 7)  # 是否返回7个分类
            self.assertIsNotNone(response['body']['twoCategoryListGoodsTop4'])  # 二级类目TOP4
            #self.assertIsNotNone(response['body']['twoCategoryListGoodsTop10'])
        except:
            raise ValueError("test_recommendPage01 faile")

    def test_recommendPage02(self):
        '''twoCategoryListGoodsTop4二级类目列表，二级商品详情字段验证'''
        print("执行test_recommendPage02")
        response = self.recommendPage()
        self.assertEqual(response['heads']['code'], 200)
        twoCategoryListGoodsTop4 = response['body']['twoCategoryListGoodsTop4']
        try:
            if twoCategoryListGoodsTop4 != None:
                for result in twoCategoryListGoodsTop4:
                    twoCategoryName = result['twoCategoryName']  # 二级类目名称
                    self.assertIsNotNone(twoCategoryName)
                    twoCategoryTitle = result['twoCategoryTitle']  # 二级类目的副标题
                    self.assertIsNotNone(twoCategoryTitle)
                    if result['topBrand'] != None:
                        for result_brand in result['topBrand']:
                            brand_price = result_brand['price']  # 价格
                            self.assertIsNotNone(brand_price)
                            goodsSourceStoreName = result_brand['goodsSourceStoreName']  # 店家名称
                            self.assertIsNotNone(goodsSourceStoreName)
                            img = result_brand['img']  # 图片
                            self.assertIsNotNone(img)
                            markDown = result_brand['markDown']  # 商品降价多少
                            self.assertIsNotNone(markDown)
                            title = result_brand['title']  # title
                            self.assertIsNotNone(title)
                            skuId = result_brand['skuId']  # 第三方skuId
                            self.assertIsNotNone(skuId)

        except:
            raise ValueError("run test_recommendPage02 false ")

    def test_shouye_threeGoods_01(self):
        '''大牌降价首页返回降价排行字段验证'''
        print("执行test_threeGoods_01")
        response = self.shouye_threeGoods(pageNum=10, currentPage=1)
        self.assertEqual(response['heads']['code'], 200)
        if response['body']['goods']!=None:
            goods = response['body']['goods']
            self.assertEqual(len(response['body']['goods']), 10)
            for result_goods in goods:
                if result_goods!=None:
                    price = result_goods['price']  # 商品价格
                    self.assertIsNotNone(price)
                    img = result_goods['img']  # 商品图片
                    self.assertIsNotNone(img)
                    markDown = result_goods['markDown']  # 商品降价价格
                    self.assertIsNotNone(markDown)
                    title = result_goods['title']  # 商品title
                    self.assertIsNotNone(title)
                    goodsCode = result_goods['goodsCode']  # 商品编号
                    self.assertIsNotNone(goodsCode)
                    goodSource = result_goods['goodSource']  # 商品来源
                    self.assertIsNotNone(goodSource)

    def test_oneCategoryPage01(self):
        '''通过recommendPage获取一级类目id验证返回字段'''
        print("执行test_oneCategoryPage01")
        response = self.recommendPage()
        self.assertEqual(response['heads']['code'], 200)
        oneCategoryList = response['body']['oneCategoryList']  # 获取一级类目列表
        self.assertIsNotNone(oneCategoryList)
        if oneCategoryList != None:
            for result_categoryOneId in oneCategoryList:
                response_data = self.oneCategoryPage(oneCategoryId=result_categoryOneId['categoryOneId'])
                self.assertEqual(response_data['heads']['code'], 200)
                self.assertIsNotNone(response_data['body'])
                twoCategoryListGoodsTop4 = response_data['body']['twoCategoryListGoodsTop4']  #
                self.assertIsNotNone(twoCategoryListGoodsTop4)

    def test_yi_threeGoods01(self):
        '''一级类目降价排行top3商品字段验证'''
        print("执行test_yi_threeGoods01")
        response = self.recommendPage()
        self.assertEqual(response['heads']['code'], 200)
        oneCategoryList = response['body']['oneCategoryList']  # 获取一级类目
        for result_data in oneCategoryList:
            response1 = self.yi_threeGoods(oneId=result_data['categoryOneId'])
            self.assertEqual(response1['heads']['code'], 200)
            goods = response1['body']['goods']  # 获取商品
            if goods != None:
                for result_goods in goods:
                    goodsCode = result_goods['goodsCode']
                    self.assertIsNotNone(goodsCode)
                    price = result_goods['price']
                    self.assertIsNotNone(price)
                    markDown = result_goods['markDown']
                    self.assertIsNotNone(markDown)
                    title = result_goods['title']
                    self.assertIsNotNone(title)

    def test_queryAllOneCategory_01(self):
        '''查询所有一级类目返回字段验证'''
        print("执行test_queryAllOneCategory_01")
        response = self.queryAllOneCategory()
        self.assertEqual(response['heads']['code'], 200)
        try:
            oneCategoryList = response['body']['oneCategoryList']
            if oneCategoryList != None:
                for result_data in oneCategoryList:
                    categoryOneId = result_data['categoryOneId']  # 一级类目id
                    self.assertIsNotNone(categoryOneId)
                    categoryOneName = result_data['categoryOneName']  # 一级类目名称
                    self.assertIsNotNone(categoryOneName)
        except:
            raise ValueError("test_queryAllOneCategory_01 faile")

    def test_queryHistoricalPrice_01(self):
        '''历史价格信息'''
        print("执行test_queryHistoricalPrice_01")
        response = self.recommendPage()
        self.assertEqual(response['heads']['code'], 200)
        goodsCode_list = []# 商品列表
        priceList_list=[]
        twoCategoryListGoodsTop4 = response['body']['twoCategoryListGoodsTop4']  # 获取二级列表
        if twoCategoryListGoodsTop4 is not None:
            for result_data in twoCategoryListGoodsTop4:
                topBrand = result_data['topBrand']  # 获取商品信息
                for result_topBrand in topBrand:
                    goodsCode = result_topBrand['goodsCode']  # 获取商品编号
                    if goodsCode not in goodsCode_list:
                        goodsCode_list.append(goodsCode)
            for result_goodsCode in goodsCode_list:
                response1 = self.queryHistoricalPrice(goodsCode=result_goodsCode)
                self.assertEqual(response1['heads']['code'], 200)
                if response1['body'] != None:
                    response1_body = response1['body']
                    if response1_body['priceDetail'] != None:
                        priceDetail = response1_body['priceDetail']  # 获取价格明细
                        priceList = priceDetail['priceList']  # 获取价格列表
                        for data_priceList in priceList:
                            if data_priceList not in priceList_list:
                                priceList_list.append(data_priceList)
                    else:
                        print("response1_body['priceDetail']值为空")
                else:
                    print("response1['body']值为空")
            try:
                for price_data in priceList_list:
                    price = price_data['price']  # 获取价格
                    self.assertIsNotNone(price)
            except:
                raise ValueError("test_queryHistoricalPrice_01 faile")


if __name__ == '__main__':
    #unittest.main()
    pytest.main(['-s', '-q', '--alluredir', './report'])

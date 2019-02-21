# -*- coding: UTF-8 -*-
from api_request import request_post, request_get
from jiexi_request_response import jiexi_json
from read_yaml import get_peizhi, write_data
from get_data import Get_data


class DapaiJiangJia(Get_data):
    def __init__(self):
       pass
    def recommendPage(self):
        '''首页推荐top4 分类下的top3品牌的top1商品'''
        url =get_peizhi(wenjianming='xiaoxiang_api', yaml_name='dapaijiangjia',
                               content_name='xiaoxiang_api_test.yaml') ['recommendPage'] # 获取url['recommendPage']
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',
                                  content_name='xiaoxiang_token.yaml')  # 获取header
        data = {'token': token}
        response = request_post(base_url=url, dict_data=data, header='')
        #print(response)
        return response

    def shouye_threeGoods(self, pageNum,currentPage):
        '''一级类目下的每个二级类目的top3商品'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='dapaijiangjia',
                               content_name='xiaoxiang_api_test.yaml')['threeGoods']
        data = {'pageNum': pageNum, 'currentPage': currentPage}  # oneCategoryId一级类目id
        response = request_post(base_url=url, dict_data=data, header='')
        #print(response)
        return response

    def oneCategoryPage(self, oneCategoryId):
        '''一级类目下的每个二级类目的top3商品'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='dapaijiangjia',
                               content_name='xiaoxiang_api_test.yaml')['oneCategoryPage']
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',
                                  content_name='xiaoxiang_token.yaml')
        data = {'token': token, 'oneCategoryId': oneCategoryId}  # oneCategoryId一级类目id
        response = request_post(base_url=url, dict_data=data, header='')
        #print(response)
        return response

    def yi_threeGoods(self, oneId):
        '''一级类目降价排行top3商品'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='dapaijiangjia',
                               content_name='xiaoxiang_api_test.yaml')['yi_threeGoods']
        data = {'oneId': oneId, 'pageNum': 10, 'currentPage': 1}  # 一级类目ID
        response = request_post(base_url=url, dict_data=data, header='')

        return response

    def er_threeGoods(self, twoId):
        '''二级类目降价排行top3商品'''
        url = self.get_url(yaml_name='dapaijiangjia')['er_threeGoods']
        data = {'twoId': twoId, 'pageNum': 10, 'currentPage': 1}  # 二级类目ID
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def queryHistoricalPrice(self, goodsCode):
        '''历史价格信息'''
        url = self.get_url(yaml_name='dapaijiangjia')['queryHistoricalPrice']
        data = {'goodsCode': goodsCode}  # 商品编号
        response = request_post(base_url=url, dict_data=data, header='')
        #print(response)
        return response

    def queryGoods(self,brandId,barId):
        '''获取二级类目下的商品列表/barId传0是为你推荐'''
        url = self.get_url(yaml_name='dapaijiangjia')['queryGoods']
        data = {'brandId':brandId,'barId':barId}
        header = self.get_header()
        response = request_post(base_url=url, dict_data=data, header=header)
        return response

    def queryBrandBar(self, brandId):
        '''获取品牌信息和二级导航以及推荐好评度最高的商品'''
        url = self.get_url(yaml_name='dapaijiangjia')['queryBrandBar']
        data = {'brandId': brandId}  # brandId品牌id
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def categoryGoods(self, categoryId):
        '''获取二级类目下的品牌以及品牌下的商品'''
        url = self.get_url(yaml_name='dapaijiangjia')['categoryGoods']
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',
                           content_name='xiaoxiang_token.yaml')
        data = {'categoryId': categoryId, 'token': token}  # 类目id
        response = request_post(base_url=url, dict_data=data, header='')
        return response

    def queryUserSubscriptionByCategory(self, token):
        '''我的订阅页面-订阅类目-查询用户订阅的二级类目的降价商品top3'''
        url = self.get_url(yaml_name='dapaijiangjia')['queryUserSubscriptionByCategory']
        data = {'token': token}  # 类目id
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def queryUserSubscriptionByBrand(self, token):
        '''我的订阅页面-订阅类目-查询用户订阅的品牌的降价商品top3'''
        url = self.get_url(yaml_name='dapaijiangjia')['categoryGoods']
        data = {'token': token}  # 类目id
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def queryUserSubscriptionByGoods(self, token):
        '''我的订阅页面-订阅类目-查询用户订阅的商品'''
        url = self.get_url(yaml_name='dapaijiangjia')['queryUserSubscriptionByGoods']
        data = {'token': token}  # 类目id
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def userSubscribe(self, type, status, id, token):
        '''我的订阅页面-订阅类目-查询用户订阅的商品'''
        url = self.get_url(yaml_name='dapaijiangjia')['userSubscribe']
        data = {'type': type, 'status': status, 'id': id, 'token': token}
        # type订阅的类型（0：商品，1：品牌，2：二级类目）
        # status  1表示需要订阅，0表示取消订阅   id品牌，类目订阅的id或者商品订阅的code
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def threeGoods(self, pageNum, currentPage):
        '''获取推荐降价排行榜top3商品'''
        url = self.get_url(yaml_name='dapaijiangjia')['threeGoods']
        data = {'pageNum': pageNum, 'status': currentPage}
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def queryPageByOneId(self, oneCategoryId):
        '''根据一级类目找二级类目，再根据二级类目找品牌'''
        url = self.get_url(yaml_name='dapaijiangjia')['queryPageByOneId']
        data = {'oneCategoryId': oneCategoryId}
        header = self.get_header()
        response = request_post(base_url=url, dict_data=data, header=header)

        return response

    def queryAllOneCategory(self):
        '''查询所有一级类目'''
        url = self.get_url(yaml_name='dapaijiangjia')['queryAllOneCategory']
        data = {}
        header=self.get_header()
        response = request_post(base_url=url, dict_data=data, header=header)
        return response

    def filterGoodsByPrice(self, oneId, brandId, twoId, priceType, sortType, pageNum,
                           currentPage):
        '''根根据商品降价幅度，降价金额来进行排序'''
        url = self.get_url(yaml_name='dapaijiangjia')['filterGoodsByPrice']
        data = {'oneId': oneId, 'brandId': brandId, 'twoId': twoId, 'priceType': priceType, 'sortType': sortType,
                'pageNum': pageNum, 'currentPage': currentPage}
        # oneId一级类目id    twoId二级类目id     sortType升序0 降序1     brandId品牌id
        # priceType幅度0 金额1
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def getFirstCategory(self):
        '''降价排行筛选一级分类获取'''
        url = self.get_url(yaml_name='dapaijiangjia')['getFirstCategory']
        data = {}
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def getChildCategory(self, childType, parentId, parentName):
        '''降价排行筛选－根据父类分类ID获取子类分类列表'''
        url = self.get_url(yaml_name='dapaijiangjia')['getChildCategory']
        data = {'childType': childType, 'parentId': parentId, 'parentName': parentName}
        # childType品类0，品牌 1      parentId父分类ID      parentName父分类名称
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def toggleUserPriceDropNotification(self, type, id, token):
        '''用户登录状态下，开启/关闭提醒'''
        url = self.get_url(yaml_name='dapaijiangjia')['toggleUserPriceDropNotification']
        data = {'type': type, 'id': id, 'token': token}
        # type订阅的类型（0：商品，1：品牌，2：二级类目）     id 品牌，类目订阅的id或者商品订阅的code
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def checkUserPriceDropNotification(self, token):
        '''降价提醒-是否有降价提醒'''
        url = self.get_url(yaml_name='dapaijiangjia')['checkUserPriceDropNotification']
        data = {'token': token}
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def queryUserPriceDropNotification(self, token):
        '''降价提醒-获取降价提醒页面的数据'''
        url = self.get_url(yaml_name='dapaijiangjia')['queryUserPriceDropNotification']
        data = {'token': token}
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response

    def filterGoods(self, oneId, brandId, twoId, priceType, sortType, pageNum,
                    currentPage):
        '''降价排行筛选降价商品'''
        url = self.get_url(yaml_name='dapaijiangjia')['filterGoods']
        data = {'oneId': oneId, 'brandId': brandId, 'twoId': twoId, 'priceType': priceType, 'sortType': sortType,
                'pageNum': pageNum, 'currentPage': currentPage}
        # oneId一级类目id    twoId二级类目id     sortType升序0 降序1     brandId品牌id
        # priceType幅度0 金额1
        response = request_post(base_url=url, dict_data=data, header='')
        print(response)
        return response


if __name__ == '__main__':
    A = DapaiJiangJia()
    goods_list=[]
    response = A.shouye_threeGoods(pageNum=10,currentPage=1)
    goods=response['body']['goods']
    print(len(response['body']['goods']))
    for result_goods in goods:
        price=result_goods['price']
        img=result_goods['img']
        markDown=result_goods['markDown']
        title=result_goods['title']
        goodsCode=result_goods['goodsCode']
        goodSource=result_goods['goodSource']
        print(goodsCode)
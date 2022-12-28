'''
pytest框架管理测试用例
默认的测试用例的规则
1模块名必须以test_开头或_test结尾
2测试类必须以Test开头
3测试方式必须以test_开头
'''


#本节课是跟随老师讲的进行写作讲解，并不是真正能跑通的接口

import requests


import pytest

def test04_func():
    print('吴桐')

class Test_Automation:

    def test_region(self):#获取地区查询
        url = 'http://apis.juhe.cn/xzqh/query'
        Headers = {'Content-Type:application/x-www-form-urlencoded'}
        data = {'fid': 650000, 'key': '0f47b877af98b78e18c3539316afafb6'}
        res = requests.post(url=url,data=data)
        print(res.json())


    def test_Model(self):#获取车型查询
        url = 'http://chehou-beta.yichehuoban.cn/sassbasic/api/serialV2/list'  # 改后增加的车型接口
        json = {"brandName": "北京奔驰", "carSerialType": "0", "cbId": 10075, "masterBrandId": "2", "saleState": "1",
                "masterBrandName": "奔驰", "serialId": 1987, "soure": "车后"}

        res = requests.post(url=url, json=json)
        print('车型返回接口',res.json())

    def test_commodity(self):#商品接口get请求
        url = 'https://chehou-beta.yichehuoban.cn/mall-goods/api/goods/op/fetch/1948'
        params = {
            "id": "1948"
        }
        respose = requests.get(url=url, params=params)  # respose是requests库返回的一个对象，简写res,respose中文叫响应
        print(respose.json())

    def test_birthday(self):#生辰查询接口
        url = 'http://apis.juhe.cn/birthEight/query'
        params={'key':'4171586eafddeec14a92c0886a23269e','year':1,'month':'4','day':'15','hour':'14'}
        res = requests.get(url=url,params=params)
        print(res.json())


if __name__ == '__main__':
    pytest.main(['-vs'])#-vs表示显示我们的调试信息





























import time
import pytest
class Testlogin:
    def  test_01_login(self):
        print('商品模块')

    @pytest.mark.smoke#mark标记测试用例用于分组执行，其中@pytest.mark是固定写法，somke是自己起的名字可以自己随意写
    def  test_02_login(self):
        print('购物车模块')


    def  test_03_login(self):
        print('支付模块')
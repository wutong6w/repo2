import time
import pytest

class Testlogin:
    def test_01_login(self):
        print('测试吴桐')

    def test_02_logao(self):
        print('测试嘿嘿')
        assert 1==2#断言1=2是失败的用例

    def test_03_login(self):

        print('测试哈哈')



if __name__ == '__main__':
    pytest.main(['-s'])







































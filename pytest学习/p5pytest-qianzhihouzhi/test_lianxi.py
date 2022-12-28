import time
import pytest

class Testlogin:

    #这个方法在所有用例执行之前只执行一次
    def setup_class(self):#类夹具，在每个测试类之前执行一次
        print('在每个类执行之前的初始化的工作：比如：创建日志对象，创建数据库的连接，创建接口的请求对象。')

    #这个方法是在每个用例执行之前执行一次
    def setup(self):#该测试夹具在每个用例执行之前执行一遍
        print('在执行测试用例之前执行的代码：打开浏览器，加载网页')

    def test_01_login(self):
        print('测试吴桐')

    def test_02_logao(self):
        print('测试嘿嘿')

    def test_03_login(self):

        print('测试哈哈')

    def test_04_login(self):
        print('测试易车')

    def teardown(self):#在每个测试用例执行之后执行一遍
        print('执行测试用例之后的扫尾工作：关闭浏览器')

    def teardown_class(self):
        print('在每个类执行后的扫尾工作：比如销毁日志对象，销毁数据库的连接，销毁接口的请求对象')

if __name__ == '__main__':
    pytest.main(['-vs'])







































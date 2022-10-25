import unittest

#对测试夹具进行封装，保证每个不同模块下的用例都能够执行直接调用
class TestJiaju(unittest.TestCase):
    @classmethod  # 注意setUpClass这个前面必须要加一个装饰器@classmethod，因为setUpClass是一个类方法
    def setUpClass(cls) -> None:
        print('setUpClass:在每个类之前执行一次。在项目当中主要用于创建数据库，生成日志对象')

    def setUp(self) -> None:  # 再每个用例之前执行遍
        print('setUp：在测试用例之前的准备工作，比如打开浏览器，加载网页')

    def tearDown(self) -> None:#在每个用例执行结束之后执行一遍
        print('tearDown:测试用例结束之后的扫尾工作，如关闭浏览器')

    @classmethod#tearDownClass也是一样的也要加上装饰器@classmethod，因为tearDownClass也是一个类方法
    def tearDownClass(cls) -> None:
        print('tearDownClass:在每个类之后执行一次。主要做一些关闭数据库链接，销毁日志对象')









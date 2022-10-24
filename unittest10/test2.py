
import unittest
from unittest10.Testfixture import TestJiaju


class Test2(TestJiaju):
    #登录用例
    def test_login(self):
        '''测试登录的'''#加上3引号注释表明该测试用例的内容，否则自动生成的html测试报告结果你不知道哪个是哪个的测试用例
        print('测试登录')
        self.assertEqual(1,2)

    def test_zhuce(self):
        '''测试注册的'''#加上3引号注释表明该测试用例的内容，否则自动生成的html测试报告结果你不知道哪个是哪个的测试用例
        print('测试注册')

















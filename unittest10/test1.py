
import unittest
from unittest10.Testfixture import TestJiaju


class Test(TestJiaju):
#测试用例
    def test01_baili(self):#在用例上运行就会运行单个测试用例，这就是单原测试
        '''测试百里的'''#加上3引号注释表明该测试用例的内容，否则自动生成的html测试报告结果你不知道哪个是哪个的测试用例
        #为什么写test01而不是test1，因为假如这个类里面有11个用例，那么到时候第11条用例不确定会第几个执行，为了更好的运行，所以就正常按照规则进行命名test01、test02
        print('测试百里')


    # 测试用例
    def test02_weiwei(self):
        '''测试薇薇的'''#加上3引号注释表明该测试用例的内容，否则自动生成的html测试报告结果你不知道哪个是哪个的测试用例
        print('测试微微')


    def test11_haha(self):
        '''测试哈哈哈哈的'''#加上3引号注释表明该测试用例的内容，否则自动生成的html测试报告结果你不知道哪个是哪个的测试用例
        print('哈哈哈哈')


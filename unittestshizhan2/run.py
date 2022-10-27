
import unittest
import os
from HTMLTestRunner import HTMLTestRunner




if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()#生成一个测试套件
    testcase = unittest.defaultTestLoader.discover(start_dir=os.path.abspath(os.path.dirname(__file__)),pattern='*.py')  # unittest调用默认加载器，在调用discover（文件夹路径，要找的文件）。意思是加载当前文件夹下的所有模块.py文件,最后生成一个用例集

    suite.addTests(testcase)  # 套件调用addtests(测试用例集)加载多个用例
    name = open(os.path.dirname(__file__) + '/report.html',
                'wb')  # open代表打开文件动作，os调用getcwd()代表的是当前路径，/代表转译，report.html是起的文件名，wb写二进制文件，对于写来说如果文件不存在则自动创建。这时当前目录下会生成一个report.html文件，可用浏览器打开
    runner = HTMLTestRunner(stream=name, verbosity=2, title='框架自动化学习测试用例',
                            description='报告详情如下：')  # HTMLTestRunner括号里传的参数（stream=文件流、也就是html报告生成的位置,verbosity=2表示详细模式测试结果会显示每个测试用例的所有相关的信息,title=测试报告标题,description=测试报告的详细情况）最后赋值给runner，那么这个runner就是html的测试运行器
    runner.run(suite)
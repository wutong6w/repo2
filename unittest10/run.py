import os

import unittest

#将运行封装在一块

if __name__ == '__main__':
    suite = unittest.TestSuite()#生成一个测试套件
    testcase = unittest.defaultTestLoader.discover(start_dir=os.getcwd(),pattern='*.py')#unittest调用默认加载器，在调用discover（文件夹路径，要找的文件）。意思是加载当前文件夹下的所有模块.py文件,最后生成一个用例集
    suite.addTests(testcase)#套件调用addtests(测试用例集)加载多个用例
    #运行方法1
    #unittest.main(defaultTest='suite')#表示只执行测试套件加载的用例，
    #运行方法2
    #unittest.TextTestRunner(verbosity=2).run(suite) #还可以使用它的运行器去运行这个套件,这两个运行方式没什么区别


'''
unittest框架--verbosity详解
0：静默模式，只能获取总的测试数和总的执行结果，比如成功3，失败4
1：默认模式，非常类似静默模式，只是在每个成功的测试用例前面会有"."，在每个失败的测试用例前面有"F"
2：详细模式，测试结果会显示每个测试用例的所有相关的信息

'''
import pytest

'''
1、主函数模式的几种方式
(1)运行所有：pytest.main()
（2）运行指定模块：
    参数详解
    -s：表示输入调试信息，包括print打印的信息   既pytest.main(['-s'])   main函数里面的参数是个列表
    -v:显示更详细信息，-s和-v可以一起使用
（3）运行指定文件夹 pytest.main(['-vs', 'pytest学习'])     其中pytest学习是文件名
（4）通过nodeid指定用例运行：node由模块名，分隔符，类名，方法名，函数名组成
         pytest.main(['-vs', './文件名/模块名.py::函数名'])
         如果要执行类里面的单个方法那么还要加类名  pytest.main(['-vs', './文件名/模块名.py::类名::函数名'])
    -n参数 pytest.main(['-vs','./文件名','-n=2'])  其中./表示当前目录    -n=2表示分布2个线程同时运行       

'''

if __name__ == '__main__':
    #pytest.main(['-vs'])#运行当前文件下所有用例（前提是运行模块与要运行的测试用例都在同级别目录）    如果在单个模块用例底下使用那么就运行单个模块的用例
    #pytest.main(['-vs','模块名.py'])运行指定模块的用例，注意用此种方法要使运行启动的模块与要执行用例的模块在统计目录，不然会找不到模块，或者前面加个文件目录也可以
    #pytest.main(['-vs', './jiekou'])#执行当前目录下接口文件夹中的测试用例，其中./代表当前目录,使用此方法要注意将该模块放在与要执行文件的同级别目录
    #pytest.main(['-vs', './jiekou/test_automation.py::test04_func'])#通过nedeid执行用例执行，例如我想执行test_automation.py里的函数test04_func就用此方法，其中：：两个双引号是分隔符
    #pytest.main(['-vs', './jiekou/test_automation.py::Test_Automation::test_region'])#使用nedeid方法执行Test_Automation类里面的方法（也就是指定执行单个测试用例）注意模块名和类名和类里面的方法名要分隔符
    #以上就是pytest的几种运行方式。下面来看pytest的分布式运行（比如4条用例分批执行需要8秒，如果开辟两个线程同时执行那么只需要4秒）
    #pytest.main(['-vs','./web','-n=4'])#其中-n=4表示分布4个线程同时运行
    pytest.main(['-vs','./web','--reruns=2'])#--reruns=2表示失败用例重跑2次，那么失败的用例就会跑3次，--reruns是固定写法，等于几就是失败后再跑几次


'''
注意：main函数里面的参数是个列表
pytest框架单独另起一个main方法，会运行本文件夹内所有的pytest用例就，就算是每个用例不在一个模块，也会运行所有的   pytest.main(['-v'])
pytest.main(['-vs'])  -v和-s可以同时用，既有打印信息也有详细的模块名和类名、用例名信息
如果想要单独某一模块的用例那么就在-vs的后面加一个参数模块名，这样就只会运行该模块的用例       pytest.main(['-vs', './test_lianxi.py'])
如果在测试中运行指定文件夹 pytest.main(['-vs', 'pytest学习'])     其中pytest学习是文件名，也就是指定执行当前文件的测试用例
'''




























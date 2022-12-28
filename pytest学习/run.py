
#此run文件是执行全局的pytest用例，（作用在全局文件的同级目录）
import pytest
import os
'''

pytest.main(['-vs'])#运行当前文件下所有用例（前提是运行模块与要运行的测试用例都在同级别目录）    如果在单个模块用例底下使用那么就运行单个模块的用例
    #pytest.main(['-vs','模块名.py'])运行指定模块的用例，注意用此种方法要使运行启动的模块与要执行用例的模块在统计目录，不然会找不到模块，或者前面加个文件目录也可以
    #pytest.main(['-vs', './jiekou'])#执行当前目录下接口文件夹中的测试用例，其中./代表当前目录,使用此方法要注意将该模块放在与要执行文件的同级别目录
    #pytest.main(['-vs', './jiekou/test_automation.py::test04_func'])#通过nedeid执行用例执行，例如我想执行test_automation.py里的函数test04_func就用此方法，其中：：两个双引号是分隔符
    #pytest.main(['-vs', './jiekou/test_automation.py::Test_Automation::test_region'])#使用nedeid方法执行Test_Automation类里面的方法（也就是指定执行单个测试用例）注意模块名和类名和类里面的方法名要分隔符
    #以上就是pytest的几种运行方式。下面来看pytest的分布式运行（比如4条用例分批执行需要8秒，如果开辟两个线程同时执行那么只需要4秒）
    #pytest.main(['-vs','./web','-n=4'])#其中-n=4表示分布4个线程同时运行
    pytest.main(['-vs','./web','--reruns=2'])#--reruns=2表示失败用例重跑2次，那么失败的用例就会跑3次，--reruns是固定写法，等于几就是失败后再跑几次

'''

if __name__ == '__main__':
    pytest.main(['-vs'])  # 运行当前文件下所有用例（前提是运行模块与要运行的测试用例都在同级别目录）    如果在单个模块用例底下使用那么就运行单个模块的用例
    # pytest.main(['-vs','模块名.py'])运行指定模块的用例，注意用此种方法要使运行启动的模块与要执行用例的模块在统计目录，不然会找不到模块，或者前面加个文件目录也可以
    # pytest.main(['-vs', './jiekou'])#执行当前目录下接口文件夹中的测试用例，其中./代表当前目录,使用此方法要注意将该模块放在与要执行文件的同级别目录
    # pytest.main(['-vs', './jiekou/test_automation.py::test04_func'])#通过nedeid执行用例执行，例如我想执行test_automation.py里的函数test04_func就用此方法，其中：：两个双引号是分隔符
    # pytest.main(['-vs', './jiekou/test_automation.py::Test_Automation::test_region'])#使用nedeid方法执行Test_Automation类里面的方法（也就是指定执行单个测试用例）注意模块名和类名和类里面的方法名要分隔符
    # 以上就是pytest的几种运行方式。下面来看pytest的分布式运行（比如4条用例分批执行需要8秒，如果开辟两个线程同时执行那么只需要4秒）
    # pytest.main(['-vs','./web','-n=4'])#其中-n=4表示分布4个线程同时运行
    #pytest.main(['-vs', './web', '--reruns=2'])  # --reruns=2表示失败用例重跑2次，那么失败的用例就会跑3次，--reruns是固定写法，等于几就是失败后再跑几次

    #pytest.main(['-vs', './p3pytestyonglizhixingshunxu'])#其中./代表是当前目录，如果是上一层目录就是../
    #pytest.main(['-vs', './p4pytest之跳过测试用例','--html=./report/report1.html'])#先自己手动在当前文件夹创建一个report的文件，代码在当前目录下-》report文件下生成report1的html文件（注意文件名最好用英文，此行文件用中文是为了自己看方便，运行时会报错（Uodek'dec无法编码字符xe4tion 11197）
    os.system('allure generate ./temp -o ./report --clean')
    #os调用system   allure generate是固定语法   ./temp表示找到你的临时报告，如果临时报告是当前文件下的其他名字如aaa，那么就是./aaa
    #-o表示输出的意思   ./report表示输出到当前的report目录下   --clean表示清空./report原来有的报告，注意是clean，不是clear













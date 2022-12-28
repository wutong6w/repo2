import time
import pytest

class Testlogin:
    age =18

    @pytest.mark.run(order=4)#用于改变测试用例的执行顺序 @pytest.mark.run是固定写法，括号里面order=4代表第4个执行的测试用例。注意要安装pytest-ordering插件，如果没有插件就算是写了此行代码也不会按照顺序执行
    def test_01_login(self):
        print('测试吴桐')

    @pytest.mark.run(order=1)#用于改变测试用例的执行顺序 @pytest.mark.run是固定写法，括号里面order=1代表第1个执行的测试用例
    def test_02_logao(self):
        print('测试嘿嘿')

    '''
    #markers参数用于标记，便于执行部分测试用例，比如执行冒烟测试用例  然后去命令行输入命令pytest -vs ./文件名 -m 'smoke'  #其中-m是参数，要执行冒烟测试用例就写上全局配置文件中smoke，如果要执行用户管理模块那么就写'username'，mark标记的smoke是自己起的名字
    全局文件中配置请看下面的markers=      标记哪些就可以配置哪些比如下面的smoke就是自己标记名，冒号后面是备注
    markers=
        smoke:冒烟测试用例
        username:用户管理模块
        proeuctmanage:接口用例
    '''
    @pytest.mark.run(order=2)  # 用于改变测试用例的执行顺序 @pytest.mark.run是固定写法，括号里面order=2代表第2个执行的测试用例
    @pytest.mark.smoke  # mark标记测试用例用于分组执行，其中@pytest.mark是固定写法，somke是自己起的名字可以自己随意写
    @pytest.mark.skipif(age>=18,reason='跳过测试用例')#有条件跳过测试用例。@pytest.mark.skipif是固定写法括号里面判断age>=18就跳过测试用例，reason=‘跳过测试用例的原因’
    def test_03_login(self):

        print('测试哈哈')

    @pytest.mark.run(order=3)#用于改变测试用例的执行顺序 @pytest.mark.run是固定写法，括号里面order=3代表第3个执行的测试用例
    @pytest.mark.username# mark标记测试用例用于分组执行，其中@pytest.mark是固定写法，username是自己起的名字可以自己随意写
    @pytest.mark.skip(reason='跳过测试用例不想执行')#@pytest.mark.skip无条件跳过测试用例，括号里可以写原因reason=‘跳过的原因’，运行的时候此条用例就不会被执行
    def test_04_login(self):
        print('测试易车')



if __name__ == '__main__':
    pytest.main(['-s'])







































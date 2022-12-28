import time
import pytest

'''
@pytest.fixture实现前后置的方法
首先写一个前后置的函数，然后在里面写前置代码，然后在yield下写后置方法，其中yield是固定代码，然后将写的函数当做参数传给需要执行前置后置的用例

将所有用例都执行前后置那么在@pytest.fixture(scope='function',autouse=True)中加个参数autouse=True就实现了所有用例都自动执行前后置
@pytest.fixture(scope='class')如果是scope='class'那么该方法就是作用在类上的，就实现每个类执行前执行一次
'''



#下面就是实现部分用例前置后置的方法
@pytest.fixture(scope='function')#使用@pytest.fixture装饰器作用于函数上，其中@pytest.fixture是固定写法，括号里scope='function'代表作用于函数
#如果是scope='class'那么该方法就是作用在类上的，就实现每个类执行前执行一次。如果是scope='modular'就会在每个模块前面执行一次
def my_fixture():#写一个函数方法
    print('这是前置的方法，可以实现部分以及全部用例的前置')
    yield #在里面加上yield，可以实现测试用例的后置方法
    print('这是后置防范，可以实现部分测试用例的后置')

class Testlogin:
    def test_01_login(self,my_fixture):#将my_fixture函数当做传参传给用例，就可以实现该用例的前置后置
        print('测试吴桐')
    def test_02_logao(self):
        print('测试嘿嘿')
    def test_03_login(self):
        print('测试哈哈')


print('------------------------------分隔符-----------------------------------')
#加上autouse=True参数实现所有用例自动执行前置后置
@pytest.fixture(scope='function',autouse=True)#使用@pytest.fixture装饰器作用于函数上，其中@pytest.fixture是固定写法，括号里scope='function'代表作用于函数,autouse=True代表默认所有用例自动使用前置后置，如果是autouse=Fales，那么就是不是自动用例都执行前后置
#如果是scope='class'那么该方法就是作用在类上的，就实现每个类执行前执行一次。如果是scope='modular'就会在每个模块前面执行一次
#如果是实现部分用例执行前后置那么就不要写autouse=True参数了，因为这个参数是让所有用例自动执行前后置的，省略了将每个用例传参函数了
def my_fixture():#写一个函数方法
    print('这是前置的方法，可以实现部分以及全部用例的前置')
    yield #在里面加上yield，可以实现测试用例的后置方法
    print('这是后置防范，可以实现部分测试用例的后置')

class Testlogin02:

    def test_01_login(self,my_fixture):#将my_fixture函数当做传参传给用例，就可以实现该用例的前置后置
        print('测试吴桐')

    def test_02_logao(self):
        print('测试嘿嘿')

    def test_03_login(self):

        print('测试哈哈')


if __name__ == '__main__':
    pytest.main(['-vs'])







































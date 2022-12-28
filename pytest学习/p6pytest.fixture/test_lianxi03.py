import pytest

#本节课讲的是@pytest.fixture装饰器中的params参数

#加上autouse=True参数实现所有用例自动执行前置后置
@pytest.fixture(scope='function',autouse=True,params=['成龙','周杰伦'],ids=['cl','zjl'])#使用@pytest.fixture装饰器作用于函数上，其中@pytest.fixture是固定写法，括号里scope='function'代表作用于函数,autouse=True代表默认所有用例自动使用前置后置，如果是autouse=Fales，那么就是不是自动用例都执行前后置
#如果是scope='class'那么该方法就是作用在类上的，就实现每个类执行前执行一次。如果是scope='modular'就会在每个模块前面执行一次
#如果是实现部分用例执行前后置那么就不要写autouse=True参数了，因为这个参数是让所有用例自动执行前后置的，省略了将每个用例传参函数了
def my_fixture(request):#写一个函数方法
    print('这是前置')
    #注意这个里面的是param，不是params，如果写params会报错，这个是系统的固定写法，装饰器参数里面才是params
    yield request.param#通过 return 语句指定返回值后，我们在调用函数时，既可以将该函数赋值给一个变量，用变量保存函数的返回值，也可以将函数再作为某个函数的实际参数
    print('这是后置')
    # return和yield都表示返回的意思，但是return后面不能有代码，yield返回后面可以接代码
class Testlogin02:

    def test_01_login(self,my_fixture):#将my_fixture函数当做传参传给用例，就可以实现该用例的前置后置
        print('测试吴桐')
        print('----------------',my_fixture)

    def test_02_logao(self):
        print('测试嘿嘿')

    def test_03_login(self):

        print('测试哈哈')


if __name__ == '__main__':
    pytest.main(['-vs'])
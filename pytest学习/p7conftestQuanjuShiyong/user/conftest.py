import pytest
#下面就是实现部分用例前置后置的方法
@pytest.fixture(scope='function')#使用@pytest.fixture装饰器作用于函数上，其中@pytest.fixture是固定写法，括号里scope='function'代表作用于函数
#如果是scope='class'那么该方法就是作用在类上的，就实现每个类执行前执行一次。如果是scope='modular'就会在每个模块前面执行一次
def user_fixture():#写一个函数方法
    print('这是uesr前置的方法，可以实现部分以及全部用例的前置')
    yield #在里面加上yield，可以实现测试用例的后置方法
    print('这是uesr后置防范，可以实现部分测试用例的后置')
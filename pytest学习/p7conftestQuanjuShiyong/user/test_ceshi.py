



class Testlogin:
    def test_01_login(self,all_fixture,user_fixture):#将user_fixture函数当做传参传给用例，就可以实现该用例的前置后置user_fixture是当前文件的前后置，all_fixture是全局的前后置，两者可以结合使用
        print('测试吴桐')
    def test_02_logao(self):
        print('测试嘿嘿')
    def test_03_login(self):
        print('测试哈哈')

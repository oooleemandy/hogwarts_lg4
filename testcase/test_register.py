'''
注册测试用例
'''
from page.main import Main


class TestRegister:

    #初始化，setup方法会在下面每个测试用例前执行
    def setup(self):
        self.main=Main()

    def test_register(self):
        #链式调用 main方法中的gotoregister，可以return到Register中的register方法
        #assert self.main.goto_register().register()
        self.main.goto_login().goto_register().register()

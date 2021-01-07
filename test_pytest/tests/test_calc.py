import yaml

from test_pytest.core.calc import Calc
import pytest
import allure



'''yaml文件驱动'''

def load_data(path='data.yaml'):
     with open(path) as f:
         data = yaml.safe_load(f)
         keys = ",".join(data[0].keys())
         values = [d.values() for d in data]
         return {'keys':keys,'values':values}

class TestCalc:

    #类执行的时候初始化一次
    def setup_class(cls):

        cls.calc=Calc()




    @allure.step
    def simple_step(self, step_param1, step_param2=None):
        pass



    #乘法的参数化
    @pytest.mark.parametrize(load_data()['keys'],load_data()['values'])
    #乘法方法
    @allure.story("乘法模块正向用例")
    def test_mult(self,a,b,c):
        #加入图片地址，图片名称，图片类型
        allure.attach.file(
            r'C:\Users\limandi\Pictures\pic\Screenshot.jpg',
            "测试图片",
            allure.attachment_type.JPG
        )
        self.simple_step(f'{a} {b} {c}')
        assert self.calc.mul(a,b) == c





    @pytest.mark.parametrize('a,b,c', [
        [1, 2, 3],
        [-1, -1, -1],
        [1, 0, 1]
    ])
    # 乘法方法
    @allure.story("乘法模块逆向用例")
    def test_mulf(self, a, b, c):
        assert self.calc.mul(a, b) == c







    @pytest.mark.parametrize('a,b,c', [
        [1, 2, "jj"],
        ["*", -1, -1],
    ])
    # 乘法方法
    @allure.story("乘法模块异常用例")
    def test_mule(self, a, b, c):
        with pytest.raises(Exception):
            assert self.calc.mul(a, b) == c













    #除法的参数化
    @pytest.mark.parametrize('d,e,f',[
        [4,2,2],
        [0.2,0.1,2],
        [0,2,0],

    ])
    #除法方法
    @allure.story("除法模块正向用例")
    def test_divt(self,d,e,f):
        assert self.calc.div(d,e) == f







    @pytest.mark.parametrize('d,e,f', [
        [36, 6, 4],
        [-10,-2,-5],
        [2.2, 2, 1]
    ])
    # 除法方法
    @allure.story("除法模块逆向用例")
    def test_divf(self, d, e, f):
        assert self.calc.div(d, e) == f




    #除数为0
    #除法的参数化
    @pytest.mark.parametrize('d,e,', [
        [2,0],
        [0.2, 0],
        [0,0],

    ])
    # 除法方法
    @allure.story("除数为0的异常处理")
    def test_dive(self, d, e):
        #返回除数为0的异常
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(d, e)



    #流程用例，比如成乘法和除法的两个用例是有调用流程的
    @allure.story("流程用例")
    def test_process(self):
        r1=self.calc.mul(1,2)
        r2=self.calc.div(2,1)
        assert r1 == 2
        assert r2 == 2
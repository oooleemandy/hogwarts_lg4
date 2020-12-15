from test_pytest.core.calc import Calc
import pytest
import allure


class TestCalc:

    def setup_class(self):
        self.calc=Calc()

    def setup(self):
        pass
    @pytest.mark.parametrize('a,b,c',[
        [1,2,2],
        [-1,-1,1],
        [1,-1,1]
    ])
    def test_mul(self,a,b,c):
        assert self.calc.mul(a,b) == c
        # assert calc.mul(-1,-1) == 1
        # assert calc.mul(1,-1) == 1

    @pytest.mark.parametrize('d,e,f',[
        [4,2,2],
        [0.2,0.1,2],
        [36,6,4]

    ])
    def test_div(self,d,e,f):
        # with pytest.raises(Exception):
        assert self.calc.div(d,e) == f


    def test_process(self):
        r1=self.calc.mul(1,2)
        r2=self.calc.div(2,1)
        assert r1 == 2
        assert r2 == 2
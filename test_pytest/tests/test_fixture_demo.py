import pytest

from test_pytest.core.calc import Calc


@pytest.fixture(scope='module')
def calc_init():
    print("calc_init")
    return Calc()

def test_calc_demo(calc_init):
    assert calc_init.mul(1,2) == 2

def test_calc_demo2(calc_init):
    assert calc_init.mul(1,3) == 3
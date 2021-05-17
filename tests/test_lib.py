from mytoolbox.lib import *


def test_factorial():
    assert factorial(6) == 720
    assert factorial(2) == 2

def test_count_down():
    assert count_down(10)[0] == 10
    assert count_down(10)[-1] == 0
    
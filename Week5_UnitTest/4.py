from calculator import square
import pytest
# 分解后就自动运行了

def test_positive():
    assert square(2) == 4
    assert square(4) == 16
    
def test_negative():
    assert square(-2) == 4
    assert square(4) == 16

# assert 适合有返回值的函数，因此尽量把

    

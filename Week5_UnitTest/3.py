from calculator import square

def test():
    assert square(2) == 4
    assert square(4) == 16
    
# 这样测试会导致遇到错误就停止，我们希望尽可能多的同时测试。
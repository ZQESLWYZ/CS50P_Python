from calculator import square

def test():
    # 引入断言进行测试
    try:
        assert square(2) == 4
    except AssertionError:
        print("断言错误1")
        
    try:
        assert square(3) == 9
    except AssertionError:
        print("断言错误2")
        
    try:
        assert square(4) == 16
    except AssertionError:
        print("断言错误3")

def main():
    test()
    
if __name__ == "__main__":
    main()
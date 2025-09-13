def hello(a):
    print("hello" + a)
    
def bybe(b):
    print("bybe" + b)
    
def main():
    hello("1")
    bybe("2")
    
if __name__ == "__main__":
    main()
    
    """
    if __name__ == "__main__":是 Python 中一个非常重要的惯用语法，它的作用是​​区分模块是被直接运行还是被导入到其他程序中​​。

核心作用：
​​模块被直接运行时​​：__name__的值是 "__main__"，条件成立，下面的代码会执行

​​模块被导入时​​：__name__的值是模块名（文件名），条件不成立，下面的代码不会执行
    """
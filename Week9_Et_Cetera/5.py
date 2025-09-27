# 指定变量和函数返回类型,然后使用mypy包检查类型

def moews(n: int) -> str:
    """Meow n times

    Args:
        n (int): The num of meows
    Returns:
        A string of meows
    """
    for _ in range(n):
        print("mewo")
        
    return "meow\n" * n 
        
number: int = int(input("Number: "))
moews(number)
meowstr: str = moews(number)
print(meowstr)
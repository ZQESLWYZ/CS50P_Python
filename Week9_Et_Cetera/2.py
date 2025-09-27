# global 全局变量
# 如果在函数内直接赋值而未声明 global，
# Python 会将其视为​​新的局部变量​​（不会修改全局变量）
# 默认全局变量只可读不可写 ❌ 触发 UnboundLocalError
# 更好的方式，使用class来管理，如3.py
balance = 0

def main():
    print("Blance", balance)
    deposit(50)
    withdraw(25)
    print("Blance", balance)

def deposit(n):
    global balance
    balance += n  
  
def withdraw(n):
    global balance
    balance -= n     
    
if __name__ == "__main__":
    main()
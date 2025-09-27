class Account:
    def __init__(self):
        self._balance = 0
    
    @property    
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n

# 体会一下封装的思想，真正的
# _balance变量不能通过外部直接访问
# 而是根据@property将方法作为属性访问
        
def main():
    account = Account()
    account.deposit(100)
    account.withdraw(50)
    print(account.balance)
    
if __name__ == "__main__":
    main()
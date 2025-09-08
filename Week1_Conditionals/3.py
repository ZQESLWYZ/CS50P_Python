# 奇偶校验
def parity(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Input an num"))
print(parity(num))
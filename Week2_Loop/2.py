a_list = [1, 2, 3, 4, 5]
b_list = list(range(3))
print(b_list)

# Pythonic编程，用下划线表示无意义的变量
for _ in range(1000):
    print("memow")

for i in a_list:
    print(i, sep=",", end=" ")
    
for i in b_list:
    print(i)
    
print("meow\n" * 3, end="")
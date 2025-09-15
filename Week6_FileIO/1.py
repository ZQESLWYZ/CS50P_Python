name = input("What's is your name? ")
print(f"{name}")

# 多个呢？
names = []

for _ in range(3):
    names.append(input("What's is your name? "))
    
print(names)

# 这样很复杂，能否将数据写入文件便于读取和分析
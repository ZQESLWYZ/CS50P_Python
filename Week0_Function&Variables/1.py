# Ask user for their name
# test comments

# TODO 1.ASK USER NAME
name = input("What's your name?\n")

# 字符串操作
name = name.strip() # 删除左右侧空格
name = name.capitalize() # 第一个单词首字母大写
name = name.title() # 所有单词首字母大写

# name = input("What's your name?\n").strip().title() # 等价操作

first_name, last_name = name.split(" ")

print(name.split(" "))

print(f"{first_name} and {last_name}")


# TODO 2.PRINT USER NAME 
print(f"Hello,{name}")
print("Hello," + name)
print("Hello,", name, name)

# 学会查阅函数文档
# print(*objects, sep=' ', end='\n', file=None, flush=False)
print("Hello,",name, sep="")

print("Hello,", end="")
print(name)

# 引号内添加引号
print("Hello,\"friend\"")
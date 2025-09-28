# Unpacking 解包list、tuple、dict，不能set
# **解包字典 → 关键字参数（​​仅当函数接受这些键作为参数名时有效​​）
a_list = [150, 200, 300]
a_tuple = (100, 200, 300)
a_dict = {
    'name1': 'Wang',
    'name2': 'Li',
}

print(*a_list)
print(*a_tuple)
print(*a_dict) 

# (base) 7.py
# 150 200 300
# 100 200 300
# name1 name2


# 解包有什么用呢，主要是向函数传参
def f(*args, **kwargs):
    print(args)
    print(kwargs)
    
f(*a_list, **a_dict)

# 更通用的形式
def f1(name, age, *args, **kwargs):
    print(name, " ", age)
    print(args)
    print(kwargs)
    
f1("Diana", 35, "London", "Doctor", salary=90000, department="Cardiology")


# 这个函数f1结合了位置参数、可变位置参数（*args）和可变关键字参数（**kwargs），调用时具有高度灵活性。以下是不同调用方式的示例：

# 示例 1：基础调用（仅必需参数）

# f1("Alice", 25)

# 输出：

# Alice   25
# ()       # args 为空元组
# {}       # kwargs 为空字典


# 示例 2：包含额外位置参数（*args）

# f1("Bob", 30, "Paris", "Engineer")

# 输出：

# Bob   30
# ('Paris', 'Engineer')  # 额外位置参数存入元组
# {}


# 示例 3：包含关键字参数（**kwargs）

# f1("Charlie", 40, city="Berlin", hobby="Reading")

# 输出：

# Charlie   40
# ()         # 无额外位置参数
# {'city': 'Berlin', 'hobby': 'Reading'}  # 关键字参数存入字典


# 示例 4：混合使用 *args 和 **kwargs

# f1("Diana", 35, "London", "Doctor", salary=90000, department="Cardiology")

# 输出：

# Diana   35
# ('London', 'Doctor')       # 额外位置参数
# {'salary': 90000, 'department': 'Cardiology'}  # 关键字参数


# 示例 5：解包参数（动态传参）

# args = ("New York", "Teacher")
# kwargs = {"married": True, "children": 2}
# f1("Evan", 28, *args, **kwargs)

# 输出：

# Evan   28
# ('New York', 'Teacher')    # 解包的位置参数
# {'married': True, 'children': 2}  # 解包的关键字参数


# 示例 6：位置参数与关键字参数混合（注意顺序）

# f1("Fiona", 50, "Sydney", role="Architect", experience=20)

# 输出：

# Fiona   50
# ('Sydney',)                # 额外位置参数
# {'role': 'Architect', 'experience': 20}


# 关键规则总结：

# 1. 前两个参数必须按位置传递（name, age）。
# 2. 后续位置参数会被收集到 args（类型为tuple）。
# 3. 关键字参数（如 key=value）会被收集到 kwargs（类型为dict）。
# 4. 调用时顺序必须是：位置参数 → *args → **kwargs。  
#    （例如：f1(name, age, *args_list, **kwargs_dict)）
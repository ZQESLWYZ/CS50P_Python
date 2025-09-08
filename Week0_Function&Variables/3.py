x = float(input("input x"))
y = float(input("input y"))
# TODO: 修复BUG
print(round(x+y, 2)) # 将浮点数四舍五入到指定位数

print(f"{(x+y):,}") # 格式化输出，加上,
print(f"{(x+y):,.2f}")
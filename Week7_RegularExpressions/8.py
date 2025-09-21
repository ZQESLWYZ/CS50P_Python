# 使用Python较新的特性--海象运算符，把赋值和询问是否为空进行合并：

import re

name = input("What's your name?")

if matchs := re.search(r"^(.+), *(.+)$", name):
    name = matchs.group(2) + ' ' + matchs.group(1)
    
print(name)
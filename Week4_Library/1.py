# 模块是一个.py文件 包是一个文件夹里面装有__init__.py文件
# 库是类似于其他编程语言的概念
# 从层级来看，库 > 包 > 模块

import random # 导入模块
from random import choice # 从模块导入函数
a_list = [1,2,3,4,99,100,22]

print(random.choice(a_list))
random.shuffle(a_list) # 就地打乱，无返回值
print(a_list)


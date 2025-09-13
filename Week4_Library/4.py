# 列表切片(左闭右开)

import sys

for arg in sys.argv[1:]:
    print(arg)
    
for arg in sys.argv[1:-1]:
    print(arg)
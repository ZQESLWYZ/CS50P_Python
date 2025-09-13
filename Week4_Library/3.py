# 命令行参数
import sys
try:
    print(sys.argv[1])
except IndexError:
    print("no")
    
if len(sys.argv) < 2:
    print("Too few arg")
elif len(sys.argv) > 2:
    print("Too many arg")
else:
    print(sys.argv[1])
    
# print(sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arg")
elif len(sys.argv) > 2:
    sys.exit("Too many arg")
else:
    print(sys.argv[1])
    
print(sys.argv[1])
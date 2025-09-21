import re


# re.search的第三个参数flag可以传递函数配置参数，支持：
# re.IGNORECASE re.MULTILINE re.DOTALL
# 忽略大小写、多行模式，改变^和$的行为针对每一行分别匹配

email = input("What's your email? ").strip()

if re.search(r"^(\w)+@\w+\.(com|org|oniline|edu)$",email,flags=re.IGNORECASE):
    print("Vaild")
else:
    print("False")
    
# 清理用户输入，也就是如果用户错误的输入我们如何处理
import re

name = input("What's your name?").strip()

matchs = re.search(r"^(.+), *(.+)$", name)

if matchs:
    print(f"Your name is {matchs.group(2)} {matchs.group(1)}")

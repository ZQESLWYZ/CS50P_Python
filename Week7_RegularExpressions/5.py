import re

email = input("What's your email? ").strip()

# \w 表示大小写字母数字和下划线 \W表示取反
if re.search(r"^(\w)+@\w+\.(com|org|oniline|edu)$",email):
    print("Vaild")
else:
    print("False")
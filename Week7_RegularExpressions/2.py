import re # 正则表达式库

# 搜索： re.search(pattern, string, flag=0)

email = input("What's your email? ").strip()

print(re.search("@", email))

if re.search("@", email):
    print("Vaild")
else:
    print("Unvaild")

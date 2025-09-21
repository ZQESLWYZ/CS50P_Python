# 检查邮箱是否有效

email = input("What's your email? ").strip()
print(email)

# if '@' in email:
#     print("Vaild")
# else:
#     print("Unvaild")

name, domain = email.split("@")

if name and domain.endswith(".edu"):
    print("valid")
else:
    print("unvaild")
# 从用户输入的X的URL中提取用户名

import re

url = input("URL: ")

# username = re.sub(r".+twitter\.com/", "", url)
username = re.sub(r"(?:https?://)?(?:www\.)?twitter\.com/"
                  ,"",url)

print(username)
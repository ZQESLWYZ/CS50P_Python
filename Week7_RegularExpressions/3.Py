import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$",email):
    print(True)
else:
    print(False)
name = input("What's is your name? ")

with open("new_names.txt", "a") as f:
    f.write(f"{name}\n")
    
# 写入会了如何读取呢？
with open("new_names.txt") as f:
    lines = f.readlines()

for line in sorted(lines, reverse=True):
    print(line.rstrip())
# open关键字
name = input("What's is your name? ")
file = open('names.txt', 'a') 
# 将w改为a表示追加模式，注意是直接的追加，不涉及自动换行之类的
print(file)
file.write(f"{name}\n")
file.close() # 关闭文件很重要，为了防止我们忘记，引入with
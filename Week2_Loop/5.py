# dic 字典

example_dic = {
    "Harry":"Grinf",
    "Ron":"Grinf",
    "Hrt":"Grinf",
}

print(example_dic.keys())
print(example_dic.values())

# 以字典名迭代只能看见key
for student in example_dic:
    print(student, example_dic[student], sep=", ")
   
# 列表字典 
dic_and_list = {
    "0":["Hermione", "Gry", "Otter"],
    "1":["Harry", "Gry", "Otter"],
    "2":["Ron", "Gry", "Otter"],
}

# 字典列表
list_and_dic = [
    {"name":"tst"},
]

print(dic_and_list)
print(list_and_dic)
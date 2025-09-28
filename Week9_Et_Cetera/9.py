# 列表推导式和字典推导式

students = ["Wang", "Li", "Qian"]
gen_list = [student.upper() for student in students]
print(*gen_list)

gen_dict = {
    student : "Griiof" for student in students
}

gen_dict2 = [
    {student : "Griiof", "age" : 18} for student in students
]

print(gen_dict)
print(gen_dict2)
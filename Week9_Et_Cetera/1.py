# set 集合

students = [
    {"name": "Wang", "house": "A"},
    {"name": "Li", "house": "B"},
    {"name": "Sun", "house": "A"},
    {"name": "Qian", "house": "C"},
    {"name": "Deng", "house": "B"},
]

houses = set()

for student in students:
    houses.add(student['house'])
    
print(sorted(houses))
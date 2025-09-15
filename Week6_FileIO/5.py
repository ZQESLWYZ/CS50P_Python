students = []

def get_name(student):
    return student['name']

with open("nameandhome.csv") as f:
    lines = f.readlines()
    
for line in lines:
    name, home = line.rstrip().split(',')
    student = {}
    student['name'] = name
    student['home'] = home
    students.append(student)
    
for student in sorted(students, key=get_name):
    print(student['name'],"is in", student['home'])
    
for student in sorted(students, key=lambda x: x['name'], reverse=True):
    print(student['name'],"is in", student['home'])
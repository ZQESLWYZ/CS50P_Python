def get_student():
    name = input("Name: ")   
    house = input("House: ")
    return {'name': name, 
            'house': house}

def main():
    # 多个返回值实际上返回了内容不可变的元组
    student = get_student()
    print(f"{student['name']} from {student['house']}")

if __name__ == "__main__":
    main()
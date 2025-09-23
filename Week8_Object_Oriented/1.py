# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")
    
# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

def get_student():
    name = input("Name: ")   
    house = input("House: ")
    return name, house

def main():
    # 多个返回值实际上返回了内容不可变的元组
    student = get_student()
    print(f"{student[0]} from {student[1]}")

if __name__ == "__main__":
    main()
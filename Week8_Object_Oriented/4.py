# raise 写条件判断自己的异常并结合 try进行处理

class Student:
    def __init__(self, name, house):
        if not (name or house):
            raise ValueError("EmptyError")
        if name not in ['Harry', 'Ron']:
            raise ValueError("WrongName")
        self.name = name
        self.house = house
    
def get_student():
    while(1):
        name = input("Name: ")
        house = input("House: ")
        try:
            student = Student(name, house)
        except ValueError:
            print("请重新输入")
        else:
            break;
    return student

def main():
    get_student()

if __name__ == "__main__":
    main()


        
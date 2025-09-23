# __str__方法用来打印实例时显示的内容

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

def main():
    print(get_student())
    

if __name__ == "__main__":
    main()


        
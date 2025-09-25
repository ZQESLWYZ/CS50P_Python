from superclass import Person

class Student(Person):
    def __init__(self, name: int, age, classes):
        super().__init__(name, age)
        self.classes = classes
        
    def __str__(self):
        return super().__str__()+ f" from {self.classes}"
        
    
if __name__ == "__main__":
    astudent = Student(10, 20, 30)
    print(astudent)

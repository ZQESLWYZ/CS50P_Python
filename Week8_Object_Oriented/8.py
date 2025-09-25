class Person:
    def __init__(self, name, age):
        self.name = name   
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} year old"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is empty")
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if not age:
            raise ValueError("Age is empty")
        self._age = age
        
    def __add__(self, other):
        name = self.name + other.name
        age = self.age + other.age
        return Person(name, age)

    @classmethod
    def get(cls, name, age):
        return cls(name, age)
    
if __name__ == "__main__":
    aperson = Person.get("Wang", 10)
    bperson = Person.get(" Yi Zhao", 10)
    print(aperson + bperson)
        
            
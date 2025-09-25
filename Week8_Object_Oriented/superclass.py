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
        
    @classmethod
    def get(cls, name, age):
        return cls(name, age)
    
    @staticmethod
    def pri(name):
        print(name)
        
    

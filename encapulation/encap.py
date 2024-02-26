

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        self.__name = value
        
    @staticmethod
    def method():
        print("Hello This is Static Method")
        

Person.method()

p = Person("Vichea", 21, "M")

print(p.Name)
p.method()

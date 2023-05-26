class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
p = Person("Anthony", 23)
print(p.getName() + " is " + str(p.getAge()))
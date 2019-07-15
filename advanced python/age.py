class Person:
    
    def __init__(self, name, age):
       self.name = name
       self.age = age
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name

Noella = Person("Noella", 2)
print(Noella.get_age())
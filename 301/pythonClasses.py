class Animal:
    type = None
    color = None
    size = None
    age = None
    def __init__(self):
        print("Class Animal Activated!")
    def chase(self, animal=None):
        return(f"I am chasing a {animal}")
    def talk(self, sound=None):
        return(sound)

class Cat(Animal):
    def __init__(self, color, size, age):
        super().__init__()
        print("Class Cat Activated!")
        self.type = "Cat"
        self.color = color
        self.size = size
        self.age = age
    def summery(self):
        print(f"I am a {self.size} {self.color} {self.type}. I am {self.age} years old!")

myAnimal = Cat("White", "Big", 7)
myAnimal.summery()
print( myAnimal.chase("Mouse") )
print( myAnimal.talk("Meow") )
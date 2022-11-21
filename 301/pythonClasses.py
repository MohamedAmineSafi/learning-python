class Animal:
    def chase(self, animal="Mouse"):
        return animal

class Dog(Animal):
    def chaseMyDog(self, animal):
        animal = super().chase(animal)
        print("I am chasing a", animal)


dog = Dog()
dog.chaseMyDog("Cat")
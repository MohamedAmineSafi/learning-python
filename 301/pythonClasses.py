# This is the syntax
# class ThisIsAnAnimal:
#     pass

# animal = ThisIsAnAnimal()

# Example
class myClass:
    this_is_a_property = ["Something", "Something Else"]

    def thisIsAMethod(self):
        print(self.this_is_a_property)
    
    def addName(self, name):
        self.this_is_a_property.append(name)
        return self.this_is_a_property

    @property
    def myMethod(self):
        return self.this_is_a_property[1]

newClass = myClass()
print(newClass.this_is_a_property)
print(newClass.addName("Meedou"))
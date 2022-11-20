# This is the syntax
# class ThisIsAnAnimal:
#     pass

# animal = ThisIsAnAnimal()

# Example
class Animal:
    this_is_a_property = ["Something", "Something Else"]

    def thisIsAMethod(self):
        print(self.this_is_a_property)
    
    @property
    def myMethod(self):
        # self.this_is_a_property.insert("Med Amine is the best")
        return self.this_is_a_property[1]

the_animal = Animal()
print(the_animal.this_is_a_property)
the_animal.thisIsAMethod()
new = the_animal.myMethod
print(new)
def myDecorator(func):
    def wrapper():
        print("Do something")
        func()
        print("Something Else")
    return wrapper

@myDecorator
def sayHi():
    print("Hi")
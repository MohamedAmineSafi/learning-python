def myGenerator():
    for num in range(10):
        yield num ** 2

list = myGenerator()
for result in list:
    print(result)
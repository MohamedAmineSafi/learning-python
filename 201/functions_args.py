def addNumbers(*args):
    numbers = args # A tuple
    t = 0
    for number in numbers:
        t = t + number
    return t

print( addNumbers(1, 2, 3, 4, 5, 6) )
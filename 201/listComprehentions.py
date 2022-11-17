list = [1, 2, 3, 4, 5]
for i, num in enumerate(list):
    list[i] = num**2


# ----------------------------------- #

anotherList = [1, 2, 3, 4, 5]
anotherList = [num**2 for num in anotherList]
print(anotherList)
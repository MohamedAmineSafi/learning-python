def person(**kwargs):
    for i in kwargs:
        print(f"Your {i} is {kwargs[i]}")

person(name="Ameen", age="31")
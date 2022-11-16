filename = input("What is the filename? ")
content = input("What is the content? ")

with open(f"201/UserFiles/{filename}.txt", 'w') as file:
    file.write(content)
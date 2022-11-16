filename = input("What is the filename? ")
content = input("What is the content? ")

with open(f"201/UserFiles/{filename}.txt", 'w') as file:
    file.write(content)

open_file = input("Would you like to read this file?")
if open_file == "y":
    with open(f"201/UserFiles/{filename}.txt", 'r') as file:
        print(file.read())
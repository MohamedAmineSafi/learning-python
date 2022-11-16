# with open("201/fileCreated.txt", 'w') as file:
#     file.write("Hello from the other side. Also, Med Amine is very handsome!")

with open("201/fileCreated.txt", 'a') as file:
    file.write("\nThis line was appended")
    file.write("\n\tThis line is tabbed")
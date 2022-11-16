# Creating big email list
# with open("201/email.txt", 'w') as file:
#     def something():
#         i=1
#         content = ''
#         while i<=100:
#             content = content + f"email{i}@gmail.com\n"
#             i = i + 1
#         return content
    
#     file.write(something())

with open("201/email.txt", 'r') as file:
    fileArr = file.readlines()
    def removeLineBreak(fileArr):
        i = 0
        for email in fileArr:
            fileArr[i] = fileArr[i][:-1]
            i = i + 1
        return fileArr
    fileArr = removeLineBreak(fileArr)

    def checkEmail(emailInput, fileArr):
        there = 0
        for email in fileArr:
            if email == emailInput:
                print("Email is there")
                there = 1
                break
        if there == 0:
            print("Email not there")
    
    checkEmail("email8@gmail.com", fileArr)
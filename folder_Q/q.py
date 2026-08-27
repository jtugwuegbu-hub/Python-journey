# import os
# cwd=os.getcwd()

# print(cwd)
# path=os.getcwd() + "/folder Q " + "/q.py"

# if os.path.exists(path):
#     print("That location exist")
#     if os.path.isfile(path):
#         print("its a file")
#     elif os.path.isdir(path):
#         print("is directory")
# else:
#     print("That location doesnt exist")


# with open("employees.txt") as file:
#     file=file.read()
#     print(file)

# with open("employees.txt") as file:
#     counter=0
#     for line in file.readlines():
#         if counter in (0,2,4):
#             data=line.split("-")
#             print(data[0])
#         counter+=1

# with open("dates.txt") as file:
#     for line in file.readlines():
#         if line != "\n":
#             data=line.split(";")
#             line=data[0].replace("/",":")
#             print(line)

numbers = open("numbers.txt","r")
result=0
with numbers as file:
    numbers= file.readlines()
for number in numbers:
    result += int(number)
result *=5
result=str(result)

with open("result.txt", "w") as file:
  file.write(str(result))
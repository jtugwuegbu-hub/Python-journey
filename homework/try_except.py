# flag=False
# while flag==False:
#     try:
#         user_input1=float(input("Pick a number?: "))
#         user_input2=float(input("Pick a number?: "))
#         user_input3=float(input("Pick a number?: "))
#         calculation=user_input1/user_input2/user_input3
#         print(calculation)
#         flag=True
#     except ValueError:
#         print("Wrong data type inserted, only interger or float")
#     except ZeroDivisionError:
#         print("You can not devide by zero")
#     finally:
#         print("file safe")
# print("done")


# def add(*LON): #LON=List of Numbers
#     LON=list(LON)
#     if LON[0]==0:
#         LON[0]=1
#     diffrence=LON[0]
#     for i in LON:
#         diffrence -=i
#     print(diffrence)

# add(0,1,1,1,1,1)

# name=input("What is your name?: ") #inputs for name, age, gender, arguments put in function parameter
# age=input("what is your age?: ") 
# gender=input("what is your gender?: ")

# def info(**person):
#     for key,val in person.items():
#         print(f"{key}:{val}")

# info(name=name, age=age)

# number=int(input("Choose a number?: "))

# def even_odd():
#     if number % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# solve=even_odd

# solve()




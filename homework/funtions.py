# def divide():
#     number=float(input("Choose number: "))
#     number= (number+10)/2
#     return number

# answer=divide()
# print(answer)

# x=float(input("number? "))
# y=float(input("number? "))
# z=float(input("number? "))

# def average(x,y,z):
#     sum_num=(x+y+z) #sum of numbers
#     average=sum_num/3 #average of numbers
#     print(f"The sum is {sum}\nThe average is {average}")
    
# average(x,y,z)

# def equation(x=3,y=3,z=3):
#     result=(x/y)*z
#     print(result)
# equation()
# equation(20,z=3,y=10)

# def loud(text): 
#    return text.upper()
   

# def quiet(text):
#    return text.lower()


# #higher order function
# def hello(func,data):
#    text = func(data) # loud("Hello") syntax for function call
#    print(text)

# print(loud)
# hello(loud,"hello") 
# hello(quiet,"HELP")


# def info():

#     name=input("What is your name?: ") #inputs for name, age, gender, arguments put in function parameter
#     for letter in name:
#         if letter in "1,2,3,4,5,6,7,8,9,0":
#             print("Your name cant have numbers")
#             info()
#     try:
#         age=int(input("what is your age?: "))
#     except ValueError:
#         print("age has to be a number")
#         info()
#     if 0<age<100:
#             pass
#     else:
#         print("age must be lest than 100 and greater than zero")
#         info()
#     print(f"name: {name}\nage: {age}")
#     return name, age
   
    

# print(info())


# def name():
#     say_name=input("What is your name?: ") #inputs for name, age, gender, arguments put in function parameter
#     for letter in say_name:
#         if letter in "1,2,3,4,5,6,7,8,9,0":
#             print("Your name cant have numbers")
#             name()
#     return say_name

# def age():
#     try:
#         say_age=int(input("what is your age?: "))
#     except ValueError:
#         print("age has to be a number")
#         return age()
#     if not 0<say_age<100:
#         print("age must be lest than 100 and greater than zero")
#         return age()
#     return say_age
    

# def info():
#     say_name=name()
#     say_age=age()
#     print(say_name,say_age)

# info()

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return(fib(n-1)+fib(n-2))

# fib(5)




def thirds(func):
    def wrapper (a):
        if a % 3 ==0 and a % 5 == 0:
            print("fizzbuzz")
        elif a % 3 == 0:
            print("fizz")
        elif a % 5 == 0:
            print("buzz")
        
        return func(a)
    return wrapper

@thirds
def divide_fizz(a):
    pass


divide_fizz(15)


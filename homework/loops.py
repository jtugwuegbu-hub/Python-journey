# count = 10

# while count>0:
#     print("*"*count)
#     count-=1

# numbers = [12,75,150,180,145,525,50]
# i=0
# while i < len(numbers):
#     number = numbers[i]
#     if number > 500:
#         break
#     elif number > 150:
#         i+=1
#         continue
#     elif number % 5 == 0:
#         print(number)
    
#     i+=1


# for number in numbers:
#     if number>500:
#         break
#     elif number>150:
#         continue
#     elif number % 5 ==0:
#         print(number)


#For loops
# cart=[10,20,30,40,50]
# total=0
# for price in cart:
#     total+=price

# print(total)

#nested loops
#rows=[5,2,5,2,2]
# for row in rows:
#     for _ in range(row):
#         print("x", end="")
#     print()

#for row in rows:
    #print("x"*row)


for x in range(3):
    for y in range(3):
        for z in range(3):
            print(f"({x},{y},{z})")
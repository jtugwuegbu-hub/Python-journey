# count = 10

# while count>0:
#     print("*"*count)
#     count-=1

numbers = [12,75,150,180,145,525,50]
i=0
while i < len(numbers):
    number = numbers[i]
    if number > 500:
        break
    elif number > 150:
        i+=1
        continue
    elif number % 5 == 0:
        print(number)
    
    i+=1


for number in numbers:
    if number>500:
        break
    elif number>150:
        continue
    elif number % 5 ==0:
        print(number)
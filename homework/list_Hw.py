list1=[1,2,3,3,2,1,3,4,6,6,8,1,4,3,2,8,4,3]
duplicate=[]
list2=[]
# for number in list1:
#     if number not in duplicate:
#         duplicate.append(number)

# print(duplicate)
while True:
    for number in list1:
        amount_num=list1.count(number)
        if amount_num<2:
            list1.remove(number)
            break
            
print(list1)
    


#math calculator
# math_list=[1,2,3,4,5]    
# squared_list=[]
# for number in math_list:
#     squared_list.append(number**2)
# print(squared_list)

#Q: you have 2 lists , list1 = [1,6,7,4,5,6], list2 = [6,5,4,2,1,5]
# for each index position , if the sum of the number from the first list and the second
# list is greater than or equal to 11 then append the numbers in a new nested list and append the index numbers
# in an another list

# list1 = [1,6,7,4,5,6]
# list2 = [6,5,4,2,1,5]
# nested_list=[]
# index_list=[]

# for index,number in enumerate(list1):
#     if number+list2[index]>=11:
#         nested_list.append([list1[index],list2[index]])
#         index_list.append(index)

# print(nested_list)
# print(index_list)
#
# 
# 
list1=[1,2,3,3,2,1,3,4,6,6,8,1,4,3,2,8,4,3]
amount=0
valid=False
number=int(input("What number are you looking for?:\n"))
user_index= int(input(f"Enter the {number} you want to find:\n"))
if list1.count(number)>0:
    for index,value in enumerate(list1):
        if value == number:
            amount+=1
            if amount == user_index:
                print(index)
                valid=True
if valid is False:
    print(f"There are {amount} in the list")



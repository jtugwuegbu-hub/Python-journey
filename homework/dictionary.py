# dict= {"Name":["Micheal Scofield","Abraham"],"Age":21,"Gender":"Male"}

# # print(dict.get("Name","Key does not exist"))
# # lists=dict.get("Name","Key does not exist")
# # dict["Name"]="Lincoln"

# dict["Name"][0]= dict["Name"][0].replace("Micheal","John") 
# dict["Name"][1]=dict['Name'][1]+" Lincoln"
# print(dict)

numbers={1:"one",2:"two",3:"three",4:"four",5:"five"}
while True:
    user_input=int(input("Pick a number 1-5: "))
    print(numbers.get(user_input,"Invalid input"))
    if (user_input in numbers)==True:
        break
        


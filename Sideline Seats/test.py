available_chairs = [0,1,2,3,4,5,6,7,8,9,10]
rented_chairs = []
damaged_chair = []
num_chairs_rent_list=[]
while True:
    print("------------------------------------------------")
    user_menu=input(             #User options
    "Please select the number from the following options?\n"
    "1.Rent chair\n"
    "2.Return chair\n"
    "3.Check inventory\n"
    "4.exit\n"
    "5.Maintance\n").lower()
    
    #Renting Chair
    if user_menu == "1" or user_menu == "rent":
        print(f"The amount of available chairs:{len(available_chairs)} chairs")# Input of how many chairs being rented
        num_chairs_rent=int(input("How many chairs would you like to rent?\n"))
        if num_chairs_rent == 0: 
            print("Select a valid number of chairs") 
            
        elif num_chairs_rent > len(available_chairs):
            print(f"There are not enough chairs to rent {num_chairs_rent}, only {len(available_chairs)} available")
            
        elif num_chairs_rent <= len(available_chairs):   #Start procces to getting them rented out
            print(f"you are about to rent out {num_chairs_rent} chairs")
            for chair in range(num_chairs_rent):
                rented=available_chairs.pop(0)
                num_chairs_rent_list.append(rented)
            while True:
                damage_input= input("Are any of the chairs damaged, if so type 'yes' if not type 'no': \n").lower() # when they rent out a chair to see if chair is damaged
                if damage_input == "yes" or damage_input == "no":
                    break
            
            if damage_input == "yes":                #What happens when chair is damaged
                for chair in num_chairs_rent_list:
                    chair_damage =input(f"Is chair {chair} damaged? 'yes' or 'no': \n").lower()
                    if chair_damage == "no":
                        rented_chairs.append(chair)
                    elif chair_damage == "yes":
                        damaged_chair.append(chair)
                    else:
                        print("invalid input")
                for chair in damaged_chair:
                            num_chairs_rent_list.remove(chair)
            elif damage_input == "no":
                rented_chairs.extend(num_chairs_rent_list)    #The final stages for user output on rented chairs
            print("you rented out chairs: ", end = "") 
            print(num_chairs_rent_list) #eventually print the code from dictionary and it will be needed to retun the chair
            print()
            num_chairs_rent_list.clear()
        
        else:
            print("Invalid statement")
            continue
            
    elif user_menu == "2" or user_menu == "return":      #When the user wants to return chairs
        print("You selected return chairs")
        num_chairs_return=int(input("How many chairs would you like to return\n")) #error handling  
        if num_chairs_return == 0:
            print("You must return 1 chair")
            
        elif num_chairs_return > len(rented_chairs):
            print("There are not that many chairs rented out")
            
        elif num_chairs_return<= len(rented_chairs):   
            for chair in range(num_chairs_return):
                chair=rented_chairs.pop(0)
                available_chairs.append(chair)
                print(f"You returned chair: {chair}")
            
        else:
            print("Invalid Statement")
            continue
            
    #Check inventory
    elif user_menu == "3" or user_menu == "inventory":
        if len(available_chairs) == 0:                 #List of chairs available
            print("There are no chairs available")
        else:
            print("Chair inventory:", end = "")
            available_chairs.sort()
            print(available_chairs)
        if len(rented_chairs)== 0:                     #list of chairs rented out
            print()
            print("No chairs rented out")
        else:    
            print()
            print("Chairs rented out:", end = "")
            rented_chairs.sort()
            print(rented_chairs)
        if len(damaged_chair)== 0:                   #list of damaged chairs
            print()
            print("No chairs damaged")
        else:    
            print()
            print("Chairs damaged:", end = "")
            damaged_chair.sort()
            print(damaged_chair)
            print()
    elif user_menu == "4" or user_menu == "exit": #for program to quit
        break
    elif user_menu == "5" or user_menu == "maintance":
        #Open menu to view damged chairs, then what chairs to put back into available
        if len(damaged_chair) == 0:
            print("There are no chairs damaged")
        else:
            print("Damaged Chairs: \n")
            damaged_chair.sort()
            print(damaged_chair)
            print()
            return_damaged_chairs=input("Would you like to make chairs available again 'yes' or 'no'? ").lower() #return chairs back into rotation
            if return_damaged_chairs == "no" and len(damaged_chair)>0:
                print(f"Chairs {damaged_chair},will remain unavailable")
            elif return_damaged_chairs == "yes" and len(damaged_chair)>0:
                for chair in damaged_chair:
                    owner_damaged_chair_control=input(f"Do you want to make chair:{chair} available again? 'yes' or 'no': ").lower()
                    if owner_damaged_chair_control == "no":
                        continue
                    elif owner_damaged_chair_control == "yes": #the control to move chairs to different list
                        available_chairs.append(chair)
                    else:
                        print("Invalid Statement")
                for chair in available_chairs:
                    if chair in damaged_chair:
                        damaged_chair.remove(chair)       
            else:
                print("Invalid Statement")
    else:
        print("Invalid statement, try again")  

print("Thank you for using Sideline seats.")                                                                                                                                                                                                                                                                                                  
        




#When the user doesnt say yes or no, i loops back to the same question and doesnt just skip the question or iteraation



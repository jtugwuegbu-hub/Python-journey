available_chairs = [1,2,3,4,5,6,7,8,9,10]
rented_chairs = []
damaged_chair = []
while True:
    print("------------------------------------------------")
    user_menu=input(
    "Please select the number from the following options?\n"
    "1.Rent chair\n"
    "2.Return chair\n"
    "3.Check inventory\n"
    "4.exit\n"
    "5.Maintance\n").lower()
    
    #Renting Chair
    if user_menu == "1" or user_menu == "rent":
        print(f"The amount of available chairs:{len(available_chairs)} chairs")# Inpt of how many chairs being rented
        num_chairs_rent=int(input("How many chairs would you like to rent?\n"))
        if num_chairs_rent == 0: 
            print("Select a valid number of chairs") 
            
        elif num_chairs_rent > len(available_chairs):
            print(f"There are not enough chairs to rent {num_chairs_rent}, only {len(available_chairs)} available")
            
        elif num_chairs_rent <= len(available_chairs):
            print(f"you are about to rent out {num_chairs_rent} chairs")
            print("you rented out chairs: ", end = "")
            for chair in range(num_chairs_rent):
                chair=available_chairs.pop(0)
                rented_chairs.append(chair)
                print(chair, end = ", ") #eventually print the code from dictionary and it will be needed to retun the chair
            print()
            damage_input= input("Are any of the chairs damaged, if so type 'yes' if not type 'no': \n") # when they rent out a chair to see if chair is damaged
            if damage_input == "no":
                continue
            elif damage_input == "yes":
                for chair in rented_chairs:
                    chair_damage =input(f"Is chair {chair} damaged: \n")
                    if chair_damage == "no":
                        continue
                    elif chair_damage == "yes":
                        damaged_chair.append(chair)
                        
                    else:
                        print("invalid input")
                for chair in damaged_chair:
                    rented_chairs.remove(chair)    
        
        else:
            print("Invalid statement")
            continue
            
    elif user_menu == "2" or user_menu == "return":
        print("You selected return chairs")
        num_chairs_return=int(input("How many chairs would you like to return\n"))
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
        if len(available_chairs) == 0:
            print("There are no chairs available")
        else:
            print("Chair inventory:", end = "")
            for chair in available_chairs:
                print(chair, end = ", ")
        if len(rented_chairs)== 0:
            print()
            print("No chairs rented out")
        else:    
            print()
            print("Chairs rented out:", end = "")
            for chair in rented_chairs:
                print(chair, end = ", ")
            print()
    elif user_menu == "4" or user_menu == "exit":
        print("Thank you come again!")
        break
    elif user_menu == "5" or user_menu == "maintance":
        #Open menu to view damged chairs, then what chairs to put back into available##
        
        if len(damaged_chair) == 0:
            print("There are no chairs damaged")
        else:
            print("Damaged Chairs: \n")
            for chair in damaged_chair:
                print(chair, end = ", ")
            print()
    else:
        print("Invalid statement, try again")                                                                                                                                                                                                                                                                                                    
        








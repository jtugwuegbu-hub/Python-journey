chair_rental_dictionary={
12:{"chair#":"chair 1","availability":True,"damage":False},
23:{"chair#":"chair 2","availability":True,"damage":False},
34:{"chair#":"chair 3","availability":True,"damage":False},
45:{"chair#":"chair 4","availability":True,"damage":False},
56:{"chair#":"chair 5","availability":True,"damage":False},
67:{"chair#":"chair 6","availability":True,"damage":False},
78:{"chair#":"chair 7","availability":True,"damage":False},
89:{"chair#":"chair 8","availability":True,"damage":False},
90:{"chair#":"chair 9","availability":True,"damage":False},
10:{"chair#":"chair 10","availability":True,"damage":False},
}
available_count=0 #To count if there are enough chairs available
checkout_counter=0 #During the proccess of gettin the amount o chairs customer wants
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
        available_count=0 #To count if there are enough chairs available
        for chair in chair_rental_dictionary.values(): #gettin amount of True from dictionary
            if chair["availability"]== True:
                available_count +=1
        print(f"The amount of available chairs:{available_count} chairs")# Input of how many chairs being rented
        num_chairs_rent=int(input("How many chairs would you like to rent?\n"))
        if num_chairs_rent == 0: 
            print("Select a valid number of chairs") 
            
        elif num_chairs_rent > available_count:
            print(f"There are not enough chairs to rent {num_chairs_rent}, only {available_count} available")
            
        elif num_chairs_rent <= available_count:   #Start procces to getting them rented out
            print(f"you are about to rent out {num_chairs_rent} chairs")
    
            while True:
                damage_input= input("Are any of the chairs damaged, if so type 'yes' if not type 'no': \n").lower() # when they rent out a chair to see if chair is damaged
                if damage_input == "yes" or damage_input == "no":
                    break
            
            if damage_input == "yes":                #What happens when chair is damaged
                checkout_counter=0
                for chair in chair_rental_dictionary:
                    if chair_rental_dictionary[chair]["availability"]==True:
                        chair_damage =input(f"Is chair {chair_rental_dictionary[chair]["chair#"]} damaged? 'yes' or 'no': \n").lower() #indivisualinput on chair damage
                        if chair_rental_dictionary[chair]["availability"]== True:
                                checkout=chair_rental_dictionary[chair]["availability"]= False
                        if chair_damage == "no":
                            pass
                        elif chair_damage == "yes":
                            chair_rental_dictionary[chair]["damage"]= True
                        else:
                            print("invalid input")
                        checkout_counter+=1
                        if checkout_counter==num_chairs_rent:
                            break
                
            elif damage_input == "no": #f the chair isnt damaged
                checkout_counter=0
                print("you rented out chairs: ")
                for chair in chair_rental_dictionary:
                    if chair_rental_dictionary[chair]["availability"]== True:
                        checkout=chair_rental_dictionary[chair]["availability"]= False
                        checkout_counter+=1
                        print(f"{chair_rental_dictionary[chair]["chair#"]} Return code:{chair} ")
                        if checkout_counter==num_chairs_rent:
                            break
                print()
            else:
                print("Invalid statement")
            
    elif user_menu == "2" or user_menu == "return":      #When the user wants to return chairs
        rented_count=0 #To count if there are enough chairs rented out
        for chair in chair_rental_dictionary.values(): #gettin amount of False from dictionary
            if chair["availability"]== False:
                rented_count +=1
        print("You selected return chairs")
        num_chairs_return=int(input("How many chairs would you like to return\n")) #error handling needed 
        if rented_count== 0:
            print("You must return 1 chair")
            
        elif num_chairs_return > rented_count:
            print("There are not that many chairs rented out")
            
        elif num_chairs_return<= rented_count:   #return procces with code verification
            num_chairs_return_counter=0
            for chair in chair_rental_dictionary:
                if chair_rental_dictionary[chair]["availability"]==False:
                    chair_return_code=int(input("Type the return code to the chair: "))
                    chair_rental_dictionary[chair_return_code]["availability"]=True
                    print(f"{chair_rental_dictionary[chair_return_code]["chair#"]} succesffully returned")
                    num_chairs_return_counter +=1
                    if num_chairs_return_counter==num_chairs_return:
                        break 

            
            
            # for chair in chair_rental_dictionary:
            #     if chair_rental_dictionary[chair]["availability"]==False:
            #         chair_return_code=int(input("Type the return code to the chair: "))
            #         for chair,info in chair_rental_dictionary.items():
            #             if chair_rental_dictionary[chair]["return_code"]== chair_return_code:
            #                 chair_rental_dictionary[chair]["availability"]=True
            #                 print(f"You successfully returned chair: {chair}")
            #                 num_chairs_return_counter+=1
            #                 break
            #             else:
            #                 print("invalid input")
            #         correct_chair_return_code=chair_rental_dictionary[chair]["return_code"]#to extract thr number from dictionary, wont do it on next for some reason
            #         if num_chairs_return==num_chairs_return_counter:
            #                 break
                
            
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

print(chair_rental_dictionary["chair1"]["return_code"])
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
#available_chairs = [0,1,2,3,4,5,6,7,8,9,10]
#rented_chairs = []
#damaged_chair = []
num_chairs_rent_list=[]

def available_chairs_count():#Function to print the available chairs
    available_count=0
    print("Chairs available:", end = "")
    for chair in chair_rental_dictionary: #gettin amount of True from dictionary
            if chair_rental_dictionary[chair]["availability"]== True and chair_rental_dictionary[chair]["damage"]==False:
                print(f"{chair_rental_dictionary[chair]["chair#"]}, ", end="")
                available_count +=1
    if available_count==0:
        print("No chairs available")
    print()
    return available_chairs_count
def rented_chairs_count():#Function to print the rented chairs
    rented_count=0
    print("Chairs rented out:", end = "")
    for chair in chair_rental_dictionary: #gettin amount of True from dictionary
            if chair_rental_dictionary[chair]["availability"]== False:
                print(f"{chair_rental_dictionary[chair]["chair#"]}, ", end="")
                rented_count +=1
    if rented_count==0:
        print("No chairs rented out")
    print()
    return rented_chairs_count
def damaged_chair_count(): #Function to print the damaged chairs
    damaged_count=0
    print("Chairs damaged:", end = "")
    for chair in chair_rental_dictionary: 
            if chair_rental_dictionary[chair]["damage"]== True:
                print(f"{chair_rental_dictionary[chair]["chair#"]}, ", end="")
                damaged_count +=1
    if damaged_count==0:
        print("No chairs damaged")
    return damaged_count
    print()
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
                        if chair_damage == "no":
                            pass
                        elif chair_damage == "yes":
                            chair_rental_dictionary[chair]["damage"]= True
                        else:
                            print("invalid input")
                        checkout_counter+=1
                        if checkout_counter==num_chairs_rent:
                            break
                checkout_counter=0
                print("you rented out chairs: ")
                for chair in chair_rental_dictionary:
                    if chair_rental_dictionary[chair]["availability"]== True and chair_rental_dictionary[chair]["damage"]==False:
                        chair_rental_dictionary[chair]["availability"]= False
                        print(f"{chair_rental_dictionary[chair]["chair#"]} Return code:{chair} ")
                        checkout_counter+=1
                        if checkout_counter==num_chairs_rent:
                            break
                print()
            elif damage_input == "no": #f the chair isnt damaged
                checkout_counter=0
                print("you rented out chairs: ")
                for chair in chair_rental_dictionary:
                    if chair_rental_dictionary[chair]["availability"]== True and chair_rental_dictionary[chair]["damage"]==False:
                        chair_rental_dictionary[chair]["availability"]= False
                        print(f"{chair_rental_dictionary[chair]["chair#"]} Return code:{chair} ")
                        checkout_counter+=1
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
            


#change how many times the loops run, it should be how many times the coustermer requested a chair and not the whole dictionary, for return and rent

        elif num_chairs_return<= rented_count:   #return procces with code verification
            num_chairs_return_counter=0
            for chair in chair_rental_dictionary:
                if chair_rental_dictionary[chair]["availability"]==False and chair_rental_dictionary[chair]["damage"]==False:
                    chair_return_code=int(input("Type the return code to the chair: ")) #to return the specific chair
                    if chair_rental_dictionary[chair_return_code]["availability"]==True: #stop chairs that are returned already
                        print("This chair is already returned")
                        continue
                    elif chair_rental_dictionary[chair_return_code]["damage"]==True: #stop chairs that are damaged
                        print("This chair is damaged, and cannot be returned")
                        continue
                    chair_rental_dictionary[chair_return_code]["availability"]=True
                    print(f"{chair_rental_dictionary[chair_return_code]["chair#"]} succesffully returned")
                    num_chairs_return_counter +=1
                    if num_chairs_return_counter==num_chairs_return:
                        break      
        else:
            print("Invalid Statement")
            continue
            
    #Check inventory
    elif user_menu == "3" or user_menu == "inventory":
        available_chairs_count() #list of chairs available
        print()
        rented_chairs_count()#list of chairs rented out
        print()
        damaged_chair_count()
        print()
    elif user_menu == "4" or user_menu == "exit": #for program to quit
        break
    elif user_menu == "5" or user_menu == "maintance":
        #Open menu to view damged chairs, then what chairs to put back into available
        damaged_chair_count_amount=damaged_chair_count()
        print()
        return_damaged_chairs=input("Would you like to make chairs available again 'yes' or 'no'? ").lower() #return chairs back into rotation
        if return_damaged_chairs == "no":
            damaged_chair_count()
            print("will remain damaged")
        elif return_damaged_chairs == "yes" and damaged_chair_count_amount>0:
            for chair in chair_rental_dictionary:
                if chair_rental_dictionary[chair]['damage']==True:
                    owner_damaged_chair_control=input(f"Do you want to make chair:{chair_rental_dictionary[chair]["chair#"]} available again? 'yes' or 'no': ").lower()
                    if owner_damaged_chair_control == "no":
                        continue
                    elif owner_damaged_chair_control == "yes": #the control to move chairs to different list
                        chair_rental_dictionary[chair]["damage"]=False
                        chair_rental_dictionary[chair]["availability"]=True       
        else:
            print("Invalid Statement or no damaged chairs")
    

print("Thank you for using Sideline seats.")


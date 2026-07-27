available_chairs = [1,2,3,4,5,6,7,8,9,10]
rented_chairs = []

while True:
    user_menu=int(input(
    "Please select the number from the following options?\n"
    "1.Rent chair\n"
    "2.Return chair\n"
    "3.Check inventory\n"
    "4.exit\n"))
    
    #Renting Chair
    if user_menu == 1:
        while True: #loop is useless aslong as it goes back to the other loop
            print(f"The amount of available chairs:{len(available_chairs)} chairs")
            num_chairs_rent=int(input("How many chairs would you like to rent?\n"))
            if num_chairs_rent == 0:
                print("Select a valid number of chairs")
                break
            elif num_chairs_rent > len(available_chairs):
                print(f"There are not enough chairs to rent {num_chairs_rent}, only {len(available_chairs)} available")
                break
            elif num_chairs_rent <= len(available_chairs):
                print(f"you are about to rent out {num_chairs_rent} chairs")
                for chair in range(num_chairs_rent):
                    chair=available_chairs.pop(0)
                    rented_chairs.append(chair)
                    print(f"You rented chairs: {chair}") #eventually print the code from dictionary and it will be needed to retun the chair
                break
            else:
                print("Invalid statement")
                break
    elif user_menu == 2:
        while True: #right now this loop is useless, but need a way for it to break
            print("You selected return chairs")
            num_chairs_return=int(input("How many chairs would you like to return\n"))
            if num_chairs_return == 0:
                print("You must return 1 chair")
                break
            elif num_chairs_return > len(rented_chairs):
                print("There are not that many chairs rented out")
                break
            elif num_chairs_return<= len(rented_chairs):
                for chair in range(num_chairs_return):
                    chair=rented_chairs.pop(0)
                    available_chairs.append(chair)
                    print(f"You returned chair: {chair}")
                break
            else:
                print("Invalid Statement")
                break
    #Check inventory
    elif user_menu == 3:
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
        








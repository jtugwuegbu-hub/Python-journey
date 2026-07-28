chair_id={
    1234:{"name":"chair 1", "available":True},
    2345:{"name":"chair 2", "available":True},
    3456:{"name":"chair 3", "available":True},
    4567:{"name":"chair 4", "available":True},
    5678:{"name":"chair 5", "available":True},
    6789:{"name":"chair 6", "available":True},
    7890:{"name":"chair 8", "available":True},
    8901:{"name":"chair 7", "available":True}
}

#start of user interaction with machine
rent_return= input("Please choose between rent and return.\n")

if rent_return=="rent":
    while True:
        rented_chairs=int(input("you selected rent, please select the amount of chairs\n"))
        if rented_chairs < 0:
            continue
        #elif rented_chair > then the amount available
            #print ("THere are not enough chairs, x amount of chairs are available right now")
            #continue
        else:
            break
    print(f"You selected {rented_chairs} chairs to rent")


while True:
    user= input("Type 'Exit' to quit or type anything to continue\n").lower()
    if user == "exit":
        break
    #age input
    age= int(input("How old are you?\n"))
    if  not 18<=age<=65:
            print("age is invalid for BMI")
            continue
    #weight input
    print("---------------------------------")
    weight=float(input("What is your weight?\n"))
    if weight <=0:
            print("Enter valid wieght")
            continue

    print("----------------------------------------")
    unit=input("Is your weight in pounds or kilograms\n").lower()
    if unit != "pounds" and unit != "kilograms":
        print("Invalid entry")
        continue
    elif unit=="pounds":
        weight*=.454 #convert to KG to calculate
    #height + BMI calculations
    print("--------------------------------------")
    height=float(input("What is your hieght in meters?\n"))
    if height <=0:
            print("Enter valid height")
            continue
    height*=height
    bmi=weight/height
    #The print of the results
    print("---------------------------------")
    print(f"Your bmi is {bmi:.2f}")
    if unit=="pounds":
        weight*=2.2046 #convert back to pounds to give results if needed
        print(f"your weight is {weight:.2f} in pounds")
    else:
        print(f"Your weight in Kilograms is {weight:.2f}")
    
    if bmi >= 25:
         print("You are overweight")
    elif bmi <=18.5:
        print("You are underweight")
    else:
        print("You are healthy and in shape")

    
print("-------------------")
print("Aplication done")
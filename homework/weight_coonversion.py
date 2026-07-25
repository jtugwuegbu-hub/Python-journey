unit= input("Select pounds or Kilograms? ").lower()
if unit=="pounds" or unit=="kilograms":
    
    weight= float(input("What is you weight? "))

    if unit=="pounds":
        pound_conversion=weight*.454
        print(f"Your weight in kilograms is {pound_conversion:.2f}.")

    elif unit=="kilograms":
        kilogram=weight*2.2046
        print(f"your weight in pounds is {kilogram:.2f}.")
else:
    print("re enter your unit and try again.")
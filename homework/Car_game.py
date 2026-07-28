car_status="stopped"

while True:
    user_input=input(">").lower()
    if user_input== "start" and car_status != "started":
        print("car is starting...")
        car_status="started"
   
    elif user_input=="start" and car_status =="started":
        print("Car is already on")
    
    elif user_input== "stop" and car_status != "stopped":
        print("The car is stopping...")
        car_status="stopped"
    
    elif user_input=="stop" and car_status == "stopped":
        print("Car is already off")
    
    elif user_input== "help":
        print(" Start-Start the car\n",
        "Stop-to stop the car\n",
        "Exit- to exit terminal",)
    
    elif user_input=="exit":
        break
    
    else:
        print("Invalid statement, type Help for controls")

print("Thanks for playing")
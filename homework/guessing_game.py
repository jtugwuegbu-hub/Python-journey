try_amounts=0
correct=26
while try_amounts<3:
    guess=int(input("Guess a number? "))
    if guess == correct:
        print("congrats you guessed correctly")
        break
    else:
        try_amounts+=1
        print(f"try again, you have used {try_amounts} trys, you have 3 max!")
    
if guess!=correct:
    print("Game over")
try_amounts=3
correct=26
while try_amounts>0:
    guess=int(input("Guess a number? "))
    if guess == correct:
        print("congrats you guessed correctly")
        break
    else:
        try_amounts-=1
        print(f"try again, you have {try_amounts} trys left")
    
if guess!=correct:
    print("Game over")
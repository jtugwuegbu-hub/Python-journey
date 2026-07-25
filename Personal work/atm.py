balance=1000
transactions=[]
print(f"your balance is ${balance}")
while True:
    user_menu=int(input(
    "Select one of the following numbers:\n"
    "1.Check Balance\n"
    "2.Deposit money\n"
    "3.Withdraw money\n"
    "4.Exit\n"
    "5.Transaction history\n"))
    if user_menu == 1:
        print(f"your balance is ${balance:,.2f}")
        print("---------------------------------")
        continue
    elif user_menu == 2:
        deposit=float(input("How much would would you like to deposit?\n"))
        if deposit<= 0:
            print("You must deposit more than 0")
            print("-------------------------------")
        else:
            balance+=deposit
        print(f"your new balance is ${balance:,.2f}")
        transactions.append(f"Deposited ${deposit:,.2f}")
        print("---------------------------------------------")
        continue
    elif user_menu == 3:
        withdraw=float(input("How much would you like to withdraw?\n"))
        if withdraw>balance:
            print(f"The amount you wish to withdraw exceeds the amunt in your account, which is ${balance:,.2f}")
            print("--------------------------------------------------------------------------------------------")
        elif withdraw<=0:
            print("You have to withdraw more than 0")
            print("----------------------------------")
        else:
            balance-=withdraw
            print(f"you withdrew ${withdraw}, your balance is now ${balance:,.2f}")
            transactions.append(f"Withdrew ${withdraw:,.2f}")
            print("------------------------------------------------------------")
            continue
    elif user_menu == 4:
        break
    elif user_menu == 5:
        if len(transactions)==0:
            print("No transactions yet")
            print("--------------------")
        else:
            print("Your transaction history")
            print("--------------------------")
            for transaction in transactions:
                print(transaction)
    else:
        print("Please pick a number from the menu again")
        print("------------------------------------------")
        continue

print("----------------------------------------")
print(f"You completed {len(transactions)} transactions.\nYour final balance is ${balance:,.2f},\nGoodbye!")
cost = int(input("What is the cost of the house? "))

credit_score=input("What is your credit? good or Bad? ").lower()

if credit_score == "good":
    good_credit=cost*.8
    print(f"Due to good credit score the house is now ${good_credit:,.2f}")

elif credit_score == "bad":
    bad_credit=cost*1.1
    print(f"sorry, becuase of your credit score, the house is now ${bad_credit:,.2f}")

else:
    print("re enter you credit score. Remember only put good or bad")
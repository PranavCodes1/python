number = int(input("enter a number between 1 to 20 \n"))
if number >=5 and number <=10:
    print("You have been selected for lucky draw \n")
    if number == 9:
        print("Hurray!! You are the Winner")
    else:
        print("You Loose,Better Luck Next Time")
else:
    print("Sorry! Not selected in draw")
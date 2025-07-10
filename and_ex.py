age = int(input("What is your age? \n"))
if age >= 18 and  age <= 40:
    print("you can participate in competition")
elif age < 18:
    print("You are too young so you cannot participate")
else:
    print("You are too old so you cannot participate")
#continue statement skips the condition we provided
number =1
while number < 8:
    number += 1
    if number % 3 == 0:
        continue
    print(f"The number is now {number}")

#repeating function

def repeat(message:str,n:int):
    msg=" "
    index = 0
    while index < n:
        msg += message
        index += 1
    return msg

r = repeat("Hi ",8)
print(r)
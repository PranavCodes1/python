sentence = input("Enter a sentence: ")
if "cat" in sentence:
    print("You are talking about cats")
    index_of_cat = sentence.find("cat")
    print(f"it starts at index {index_of_cat}")
else:
    print("You are talking about something else")
number = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if number.strip() == "42" or number.lower().strip() == "forty-two" or number.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")

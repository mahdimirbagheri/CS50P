import validators

address = input("What's your email address? ").strip()

if validators.email(address) == True:
    print("Valid")
else:
    print("Invalid")

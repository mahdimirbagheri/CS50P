dollars = 0
greet = input("Greeting: ").strip().upper()
if greet.startswith("HELLO"):
    print(f"${dollars}")
elif greet.startswith("HOW"):
    print(f"${dollars + 20}")
elif greet.startswith("WHAT"):
    print(f"${dollars + 100}")

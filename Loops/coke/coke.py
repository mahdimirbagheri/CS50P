due = 50
gain = 0

while gain < due:

    print(f"Amount Due: {due - gain}")
    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        gain += coin

    else:
        continue

    print(f"Change Owed: {-(due - gain)}")

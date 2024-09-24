grocery = {}

while True:
    try:
        item = input().upper().strip()
        if item not in grocery:
            # Initialize item's qty in shoplist (grocery)
            grocery[item] = 1
        else:
            # Update item's qty
            grocery[item] = grocery[item] + 1

    except EOFError:
        sorted_grocery = dict(sorted(list(grocery.items())))
        for item in sorted_grocery:
            print(f"{sorted_grocery[item]} {item}")
        break
    except KeyError:
        pass

while True:
    # TODO : Input tank
    tank = input("Fraction: ").strip()
    # TODO : Handeling errors in deviding with try except
    try:
        # TODO : Splitting input
        x, y = tank.split("/",1)
        # TODO : Cheak numbers
        if x.isdigit and y.isdigit():
            # TODO : make typy of input!?
            if int(x) <= int(y) and int(y) != 0:
                fuel = (int(x) / int(y)) * 100
                if fuel >= 99:
                    print("F")
                    break
                elif fuel < 99 and fuel > 1:
                    print(f"{fuel:.0f}%")
                    break
                else:
                    print("E")
                    break
    except (ValueError, ZeroDivisionError):
        pass
    else:
        pass

def main():
    while True:
    # TODO : Input tank
        try:
            tank = input("Fraction: ").strip()
            print(gauge(convert(tank)))
            break
        # TODO : Handeling errors in deviding with try except
        except (ValueError, ZeroDivisionError, UnboundLocalError):
            continue


def convert(fraction):
    if "/" in fraction:
        # TODO : Splitting input
        x, y = tank.split("/",1)

    else:
        raise UnboundLocalError("Not a valid fraction")

    # TODO : Cheak numbers
    if x.isdigit() and y.isdigit():
         # TODO : make typy of input!?
         if int(x) <= int(y) and int(y) != 0:
              fuel = (int(x) / int(y)) * 100
              return fuel
         else:
              raise ZeroDivisionError("X is larger than Y")
    else:
         raise ValueError("Not an integer")


def gauge(percentage):
    if int(percentage) >= 99:
        return "F"

    elif int(percentage) < 99 and int(percentage) > 1:
        return f"{percentage:.0f}%"
    else:
        return "E"


if __name__ == "__main__":
    main()










    except (ValueError, ZeroDivisionError):
        pass
    else:
        pass

import sys
import requests

apilink = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    print(f"${btc_coin(test()):,.4f}")


# TODO : TESTING USER INPUT


def test():
    try:

        if len(sys.argv) < 2:
            print("Missing command-line argument")
            sys.exit(1)

        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")
            sys.exit(1)

        else:
            return float(sys.argv[1])

    except (TypeError, ValueError):
        print("Command-line argument is not a number")
        sys.exit(1)


# TODO : GET BTC PRICE FROM JSON FILE


def btc_coin(uinput):
    try:
        response = requests.get(apilink)
        result = response.json()
        price = result["bpi"]["USD"]["rate_float"]
        total = uinput * price

    except requests.RequestException:
        print("CONNECTION ERROR!")
        sys.exit()

    return total


if __name__ == "__main__":
    main()

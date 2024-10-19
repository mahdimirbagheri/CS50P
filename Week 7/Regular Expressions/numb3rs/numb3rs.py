import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        octed = ip.split(".", maxsplit=3)
        for octeds in octed:
            if int(octeds) > 255 or len(octed) < 4:
                return False
    except ValueError:
        return False

    else:
        return True


if __name__ == "__main__":
    main()

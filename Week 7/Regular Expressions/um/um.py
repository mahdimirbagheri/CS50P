import re


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()

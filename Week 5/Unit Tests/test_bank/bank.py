def main():
    greet = input("Greeting: ").strip().upper()
    print(f"${value(greet)}")


def value(greeting):

    if greeting.startswith("HELLO"):
        return 0
    elif greeting.startswith("HOW"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = str(input("Name: ")).strip()
        names.append(name)
    except (EOFError, KeyError):
        print(f"Adieu, adieu, to {p.join(names)}", end="\n")
        break

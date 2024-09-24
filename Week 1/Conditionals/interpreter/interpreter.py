# TODO : Make Input
x, y, z = input("Expression: ").strip().split(" ")
# TODO : Checking Operator
match y:
    case "+":
        answer = float(x) + float(z)
    case "-":
        answer = float(x) - float(z)
    case "/":
        answer = float(x) / float(z)
    case "*":
        answer = float(x) * float(z)
    case _:
        exit(1)
print(f"{answer:.1f}")

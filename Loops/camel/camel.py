camels = input("camelCase: ").strip()
snake = ""
for camel in camels:
    if camel.isupper():
        snake += "_"
        snake += camel.lower()
    else:
        snake += camel

print(f"snake_case: {snake}")

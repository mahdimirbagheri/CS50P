from emoji import emojize
input = str(input("Input: ").strip())
print(f"Output: {emojize(input, language='alias')}")

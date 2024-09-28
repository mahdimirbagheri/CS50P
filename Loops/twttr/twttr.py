vowels = ["a", "e", "i", "u", "o"]
output = ""
texts = input("Input: ").strip()

for text in texts:
    if text.lower() not in vowels:
        output += text

print(f"Output: {output}")

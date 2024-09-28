vowels = ["a", "e", "i", "u", "o"]

def main():
    texts = input("Input: ").strip()
    print(f"Output: {shorten(texts)}")


def shorten(word):
    output = ""

    for text in word:
    if text.lower() not in vowels:
        output += text

    return output

if __name__ == "__main__":
    main()

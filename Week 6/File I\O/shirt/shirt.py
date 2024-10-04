import sys
import os
from PIL import Image, ImageOps


def main():
    # cheak command-line arg
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 3:
        print("Too few command-line arguments")
        sys.exit(1)

    elif not os.path.isfile(sys.argv[1]):
        print(f"Invalid input _ path")
        sys.exit(1)

    elif not fcheck(sys.argv[1]) and fcheck(sys.argv[2]):
        print(f"Invalid input")
        sys.exit(1)

    elif not fsame(sys.argv[1], sys.argv[2]):
        print(f"Input and output have different extensions")

    else:
        # Pass
        shirtwear(sys.argv[1], sys.argv[2])


def fcheck(input):
    format = [".jpg", ".jpeg", ".png"]
    _, cf = input.split(".", maxsplit=1)

    if cf in format:
        return True
    else:
        return False


def fsame(input, output):

    _, cf = input.split(".", maxsplit=1)

    if output.endswith(cf):
        return True
    else:
        return False


def shirtwear(input, output):

    shirt = Image.open("shirt.png")
    uimg = Image.open(input)

    a, b = shirt.size
    uimg = ImageOps.fit(uimg, (a, b))

    uimg.paste(shirt, shirt)
    uimg.save(output)


if __name__ == "__main__":
    main()

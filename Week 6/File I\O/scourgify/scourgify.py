
import os
import csv
import sys
from tabulate import tabulate


def main():

    # cheak command-line arg
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    elif not os.path.isfile(sys.argv[1]):
        print(f"C dose not exist")
        sys.exit(1)

    elif not sys.argv[1].endswith(".csv"):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

    else:
        # pass
        scourgify(sys.argv[1], sys.argv[2])


def scourgify(input, output):
    # Convert Before Format To End Format
    with open(input) as input:

        reader = csv.DictReader(input)
        with open(output, "w") as output:

            header = ["first", "last", "house"]

            writer = csv.DictWriter(output, fieldnames=header)

            writer.writeheader()

            for student in reader:
                last, first = student["name"].split(", ")
                house = student["house"]
                writer.writerow({"first": first, "last": last, "house": house})


if __name__ == "__main__":
    main()

import os
import csv
import sys
from tabulate import tabulate


def main():

    # cheak command-line arg
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    elif not os.path.isfile(sys.argv[1]):
        print("File dose not exist")
        sys.exit(1)

    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    else:
        tabulize(sys.argv[1])


def tabulize(file):
    with open(file, "r") as csv_file:
        table = csv.DictReader(csv_file, delimiter=",")
        print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()

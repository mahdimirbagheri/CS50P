from datetime import date
import sys
import inflect
import operator
engine = inflect.engine()


def main():
    try:
        dates = input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(dates))
        print(textout(difference.days))

    except ValueError:
        sys.exit("Invalid date")


def textout(time):
    min = time * 24 * 60
    return f"{(engine.number_to_words(min, andword="")).capitalize() + " minutes"}"


if __name__ == "__main__":
    main()

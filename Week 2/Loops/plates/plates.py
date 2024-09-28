symbols = [" ", ".", "?", "!", ",", ":", ";",
           "(", ")", "[", "]", "'", "-", '"', "/", "\\", "`", "@", "#", "*", ]


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validated = ""
    numcheck = 0

    # TODO : Checking the length of letters 2 to 6
    if len(s) >= 2 and len(s) <= 6:

        # TODO : Checking whether characters 1 and 2 are correct
        if s[0].isalpha() and s[1].isalpha():

            for ch in s:
                # TODO : Checking the absence of symbols of letters
                if ch not in symbols:

                    # TODO : Checking that the first number is not zero
                    if ch.isnumeric() and numcheck == 0 and ch != "0":
                        numcheck += 1
                        validated += ch

                    # TODO : Checking if the number is greater than zero
                    elif ch.isnumeric() and numcheck > 0:
                        numcheck += 1
                        validated += ch

                    # TODO : Checking that the text does not start with a number
                    elif ch.isalpha() and numcheck == 0:
                        validated += ch

    if validated == s:
        return True
    else:
        return False


main()

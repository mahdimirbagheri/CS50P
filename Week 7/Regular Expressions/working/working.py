import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    condition = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + condition + " to " + condition + "$", s)
    if match:
        from_time = standardsize(match.group(1), match.group(2), match.group(3))
        time = standardsize(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {time}"
    else:
        raise ValueError


def standardsize(hr, min, x):
    if hr == "12":
        if x == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if x == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12}"
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()

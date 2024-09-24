months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        # TODO : Get date from user
        date = input("Date: ").strip()
        # TODO : cheaking date format with month name Like = (September 8, 1636)
        if " " in date:
            if "," in date:
                month, day, year = date.split(" ")
                # TODO : Founding month in lists and Deleteing "," after dey and convert month name to month number
                if month.title() in months:
                    day = int(day.strip(","))
                    month = int(months.index(month)) + 1
                    # TODO : Check month and day range
                    if month <= 12 and day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break
        # TODO : cheaking date format Like = (9/8/1636)
        else:
            month, day, year = date.split("/")
            if int(month) <= 12 and int(day) <= 31:
                print(f"{int(year)}-{int(month):02}-{int(day):02}")
                break
    # TODO : Error Handeling
    except ValueError:
        continue

    except (EOFError, KeyboardInterrupt):
        print("", end="\n")
        quit()

    else:
        continue

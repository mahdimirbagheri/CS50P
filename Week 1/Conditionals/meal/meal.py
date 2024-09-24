def main():

    # TODO : Meals?

    meals = [
        {"meal": "breakfast time", "start": 7, "end": "8"},
        {"meal": "lunch time", "start": 12, "end": 13},
        {"meal": "dinner time", "start": 18, "end": 19}
    ]
    time = input("What time is it? ")
    time = float(convert(time))

    # TODO : Search Meal

    for meal in meals:
        if time >= float(meal["start"]) and time <= float(meal["end"]):
            print(meal["meal"])
        else:
            continue


def convert(time):
    start = 0.0

    if time.rfind(" a.m.") != -1:
        time = time.replace(" a.m.", "")

    elif time.rfind(" p.m.") != -1:
        time = time.replace(" p.m.", "")
        start = 12.0

    hours, minutes = time.strip().split(":")
    time2 = float(hours) + start + (float(minutes) / 60)
    return time2


if __name__ == "__main__":
    main()

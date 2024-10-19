import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(links):

    try:
        link = re.search('(?<=embed\/).*?(?=")', links)
        return "https://youtu.be/" + link.group(0)
    except Exception:
        return None


if __name__ == "__main__":
    main()

import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
fontlist = figlet.getFonts()

if len(sys.argv) == 1:
    input = input("Input: ").strip()
    figlet.setFont(font=choice(fontlist))
    print(figlet.renderText(input))

elif len(sys.argv) == 3:

    if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in fontlist:
        input = input("Input: ").strip()
        figlet.setFont(font=str(sys.argv[2]))
        print(figlet.renderText(input))

    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

import sys
import pyfiglet

if len(sys.argv) == 1:
    text = input("Input: ")
    figlet = pyfiglet.Figlet()
    print(figlet.renderText(text))

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    text = input("Input: ")
    figlet = pyfiglet.Figlet(font=sys.argv[2])
    print(figlet.renderText(text))

else:
    sys.exit("Invalid usage")

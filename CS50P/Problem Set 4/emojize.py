from emoji import emojize

def main():
    code = input("Input: ")
    emoji(code)

def emoji(code):
    print(emojize(code,language = "alias"))

main()
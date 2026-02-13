def main():
    greeting = input("Enter Your Greetings: ").strip()
    print(value(greeting))

def value(greeting):
    if greeting.startswith(("hello","Hello","HELLO")) == True:
        return "$0"
    elif greeting.startswith(("h","H")) == True:
        return "$20"
    else:
        return "$100"
    
if __name__ == "__main__":
    main()
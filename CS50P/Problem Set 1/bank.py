def main():
    greeting = input("Enter Your Greetings: ").strip()
    print(kramer(greeting))

def kramer(greeting):
    if greeting.startswith(("hello","Hello")) == True:
        return "$0"
    elif greeting.startswith(("h","H")) == True:
        return "$20"
    else:
        return "$100"
    
main()
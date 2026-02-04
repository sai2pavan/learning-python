def main():
    n = get_number()
    meow(n)

def get_number():
    while True:
        number = int(input("what's n? "))
        if number > 0:
            return number
        break

def meow(n):
    print("meow\n" * n, end = "")

main()
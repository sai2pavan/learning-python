#ask use for an input
def main():
    number = int(input("enter a number: "))
    print("Even") if is_even(number) == True else print("Odd")
#check if the number is even or odd
def is_even(x):
    return (x % 2 == 0)

main()
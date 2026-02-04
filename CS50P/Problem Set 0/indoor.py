#take input from user
def main():
    n = input("Speak ")
    print(lowercase(n))
#convert the input into lower case
def lowercase(n):
    n = n.lower()
    return n
main()
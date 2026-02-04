def main():
    str = input("Input: ")
    print("Output:",omitted(str))

vowels = ["a","e","i","o","u","A","E","I","O","U"]

def omitted(string):
    output = ""
    for i in string:
        if i in vowels:
            continue
        else:
            output += i
    return output

main()
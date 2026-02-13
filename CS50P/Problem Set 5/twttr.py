def main():
    full = input("Input: ")
    print("Output:",shorten(full))

vowels = ["a","e","i","o","u","A","E","I","O","U"]

def shorten(string):
    output = ""
    for i in string:
        if i in vowels:
            continue
        else:
            output += i
    return output

if __name__ == "__main__":
    main()
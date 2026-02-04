def main():
    camelcase = input("camelCase: ")
    print("snake_case:",snake_case(camelcase))

def snake_case(name):
    result = ""
    for i in name:
        if i.isupper():
            result += "_" + i.lower()
        else:
            result += i
    return result

main() 
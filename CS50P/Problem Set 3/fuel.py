def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)

            if x > y:
                continue

            percent = round((x/y) * 100)
            
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(str(percent) + "%")
            break
        except (ValueError, ZeroDivisionError):
            pass
main()


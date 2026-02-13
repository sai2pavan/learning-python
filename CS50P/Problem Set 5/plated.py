def main():
    plate = input("PLATE: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Rule 1: Length between 2 and 6
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Rule 2: First two characters must be letters
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    # Rule 3: Only alphanumeric characters allowed
    for c in plate:
        if not c.isalnum():
            return False

    # Rule 4: Numbers, if present, must be at the end
    # and the first number cannot be 0
    number_started = False
    for c in plate:
        if c.isdigit():
            if not number_started:
                if c == "0":
                    return False
                number_started = True
        else:
            if number_started:
                return False

    return True


if __name__ == "__main__":
    main()
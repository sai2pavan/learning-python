ans = input("What is the answer to the Great Question of life, the Universe and Everything? ")
match ans:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
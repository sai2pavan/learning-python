def main():
    score = int(input("Score: "))
    print("Grade:",grade(score))

def grade(x):
    if x >= 90:
        return ("A")
    elif x >= 80:
        return ("B")
    elif x >= 70:
        return ("C")
    elif x >= 60:
        return ("D")
    else:
        return ("F")
    
main()
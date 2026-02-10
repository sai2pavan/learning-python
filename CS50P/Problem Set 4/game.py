import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

numb = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue    
    if guess > numb:
        print("Too large!")
    elif guess < numb:
        print("Too small!")
    else:
        print("Just right!")
        break

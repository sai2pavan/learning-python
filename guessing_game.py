import random

replay = "yes"
print("I'm thinking of a number!(between 1 to 100) Try to guess the number:")

while replay == "yes":
    initial = random.randint(1,100)
    guess = -1
    
    

    while guess != initial:
        guess = int(input())
        if guess > initial:
            print("too high! try again.")
        elif guess < initial:
            print("too low! try again.")
        else:
            print("Thats it! Thats the guess!")
    replay = input("would you like to play again (yes/no)").lower().strip()

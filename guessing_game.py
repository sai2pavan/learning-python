import random

replay = "yes"
print("🎮 WELCOME TO THE NUMBER GUESSING GAME 🧠\n"
      "Guess a number between 1 to 100\n"
      "After each Guess you will be given hint on how far you are from the number\n"
      "Good Luck!")

while replay == "yes":
    print("I'm thinking of a number!(between 1 to 100) Try to guess the number:")
    initial = random.randint(1,100)
    guess = -1
    
    

    while guess != initial:
        guess = int(input())
        difference = guess - initial
        if difference > 10:
            print("Higher!")
        elif difference < -10:
            print("Lower!")
        elif 10 >= difference >= 5:
            print("High!")
        elif -10 <= difference <= -5:
            print("Low!")
        elif 5 > difference > 0:
            print("Near! But High")
        elif -5 < difference < 0:
            print("Near! But Low")
        else:
            print("Thats it!", initial, "is the guess")
    replay = input("would you like to play again (yes/no)").lower().strip()

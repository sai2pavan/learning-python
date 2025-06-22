import random

replay = "yes"
print("\tWELCOME TO THE NUMBER GUESSING GAME\n"
      "\tGuess a number between 1 to 100\n"
      "\tAfter each Guess you will be given hint on how far you are from the number\n"
      "\tGood Luck!")
print()

while replay == "yes":
    initial = random.randint(1,100)
    guess = -1
    
    

    while guess != initial:
        guess = int(input("\tI'm thinking of a number!(between 1 to 100) Try to guess the number:"))
        difference = guess - initial
        if difference > 10:
            print("\tHigher!")
        elif difference < -10:
            print("\tLower!")
        elif 10 >= difference >= 5:
            print("\tHigh!")
        elif -10 <= difference <= -5:
            print("\tLow!")
        elif 5 > difference > 0:
            print("\tNear! But High")
        elif -5 < difference < 0:
            print("\tNear! But Low")
        else:
            print("\tThats it!", initial, "is the number")
    replay = input("\twould you like to play again (yes/no)").lower().strip()

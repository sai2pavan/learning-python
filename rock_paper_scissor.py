import random
print("Hello and welcome to ROCK, PAPER and SCISSORS game")
replay = "yes"

while replay == "yes":
    plays = ["rock","paper","scissors"]
    cc = random.choice(plays)
    uc = input("Enter your choice in rock, paper and scissors:").lower().strip()

    if cc == uc:
        print("Its a Draw, you both have put", cc)
    elif cc == "rock" and uc == "paper":
        print("Paper eats the rock.\nYou have won")
    elif cc == "paper" and uc == "rock":
        print("Paper eats rock.\nYou have lost")
    elif cc == "paper" and uc == "scissors":
        print("Scissor cuts paper.\nYou have won")
    elif cc == "scissors" and uc == "paper":
        print("Scissors cuts paper\nYou have lost")
    elif cc == "scissors" and uc == "rock":
        print("Rock breaks scissors\nYou have won")
    elif cc == "rock" and uc == "scissors":
        print("Rock Breaks scissors\nYou have lost")

    replay = input("would you like to play again? (yes/no)")
    

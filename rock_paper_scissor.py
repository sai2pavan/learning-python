import random
print("\tWELCOME TO THE ROCK, PAPER AND SCISSORS GAME\n\tITS A 3 ROUND MATCH\n\tWHOEVER WINS MAXIMUM ROUNDS WINS!")
replay = "yes"

while replay == "yes":
    plays = ["rock","paper","scissors"]
    comp = 0
    user = 0
    
    for i in range(1,4):
        print()
        print("\tROUND",i)
        cc = random.choice(plays)
        while True:
            uc = input("\tEnter your choice in rock, paper and scissors:").lower().strip()
            if uc in plays:
                break
            print("\tInvalid input, please select a choice from rock, paper and scissors")
            
        if cc == uc:
            print("\tIts a Draw, you both have put", cc.upper())
        elif cc == "rock" and uc == "paper":
            print(f"\t{uc.upper()} beats {cc.upper()}")
            user += 1
        elif cc == "paper" and uc == "rock":
            print(f"\t{cc.upper()} beats {uc.upper()}")
            comp += 1
        elif cc == "paper" and uc == "scissors":
            print(f"\t{uc.upper()} beats {cc.upper()}")
            user += 1
        elif cc == "scissors" and uc == "paper":
            print(f"\t{cc.upper()} beats {uc.upper()}")
            comp += 1
        elif cc == "scissors" and uc == "rock":
            print(f"\t{uc.upper()} beats {cc.upper()}")
            user += 1
        elif cc == "rock" and uc == "scissors":
            print(f"\t{cc.upper()} beats {uc.upper()}")
            comp += 1

    print("\tCOMPUTER",comp,"-",user,"USER")
    if comp > user:
        print("\tYOU HAVE LOST, BETTER LUCK NEXT TIME")
    elif user > comp:
        print("\tYOU HAVE WON, WELLPLAYED")
    else:
        print("\tITS A DRAW, BETTER LUCK NEXT TIME")
    replay = input("would you like to play again? (yes/no)").lower().strip()
    

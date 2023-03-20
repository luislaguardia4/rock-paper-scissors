#group name: Awit
#leader and member:  Luis Laguardia

import random

awit = input("Enter a choice (rock, paper, scissors):\n ")

rps = ["rock", "paper", "scissors\n"]
meAI = random.choice(rps)

error = "please choose one: rock, paper, scissors\n"

if awit != rps:
  print(error)
# quit()

print ("sing... Rock, Scissors, Paper x2, one two three")
print ("\nplay with me :>\n")

print(f"\nI chose {meAI}, You chose {awit}.\n")

#import random is to import random module in my program or the game...
#awit will be the command caller when the user inputs rps
#and the random.choice

if awit == meAI:
    print(f"Both of us selected {awit}. It's a tie! hehe")
elif awit == "rock":
    if meAI == "scissors":
        print("Rock can break scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif awit == "paper":
    if meAI == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif awit == "scissors":
    if meAI == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else:
    print("invalid")
#it will print invalid if u didn't input rock, paper, and scissors

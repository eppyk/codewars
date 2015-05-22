### The idea was taken from here:
http://www.reddit.com/r/beginnerprojects/comments/2ah82f/rock_paper_scissors/
###

import random

def game():
    r = "rock"
    p = "paper"
    s = "scissors"

    users_pick = input("Rock, paper or scissors, mate? \n")

    our_pick = random.choice([p, r, s])
    print ("My pick is: " + our_pick + "! Sooo...")

    if users_pick==r:
        if our_pick==p:
            print("YOU LOOSE!")
            return "comp"
        else:
            print("YOU WIN!")

    elif users_pick==p:
        if our_pick==s:
            print("YOU LOOSE!")
            return "comp"
        else:
            print("YOU WIN!")

    elif users_pick==s:
        if our_pick==r:
            print("YOU LOOSE!")
            return "comp"
        else:
            print("YOU WIN!")


score_comp = 0
score_user = 0
decision = input("Hello, this is computer. Wanna play rock, paper, scissors? y/n\n")

while decision != "n":

    if game()=="comp":
        score_comp += 1
        decision = input("Still wanna play? y/n \n")
    else:
        score_user += 1
        decision = input("Still wanna play? y/n \n")

print("The scores are the following: \n I've got %d points\n You've got %s points \n" %(score_comp, score_user))

if score_comp > score_user:
    print("I WIN, LOOSER!")
else:
    print("I guess you've just proven to be smarter than a machine...")

'''
WORKFLOW OF PROJECT:

1- Input from the user(Rock, Paper, Scissor).
2- Computer choice (It will choose randomly not conditionally).
3- Result Print.

Cases:

A- Rock
Rock - Rock = tie
Rock - Paper = paper win
Rock - Scissor = rock win

B- Paper
Paper - Paper = tie 
Paper - Rock = paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = rock win
Scissor - Paper = Scissor win


'''
import random

item_list=["Rock","Paper","Scissor"]

user_choice = input("Enter your move(Rock, Paper, Scissor): ")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both Choose Same: It's Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock: Computer Win")
    else:
        print("Rock Smashes Scissor: You Win")
elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper Covers Rock: You Win")     
    else:
        print("Scissor Cuts Paper: Computer Win")
elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock Smashes Scissor: Computer Win")
    else:
        print("Scissor Cuts Paper: You Win")
else:
    print("Incorrect Choice!, Please Choose from the options.")


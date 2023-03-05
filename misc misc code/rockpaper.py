import random
rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
winning_score = 3
computer_score = 0
user_score = 0
while computer_score < winning_score and user_score < winning_score:
    user_choice = input("choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    if user_choice == computer_choice:
        print("it's a tie")
    elif rules[user_choice] == computer_choice:
        print("you win")
        user_score += 1
    else:
        print("computer wins")
        computer_score += 1
    print(f"your score: {user_score}\tcomputer score: {computer_score}\n")
if user_score > computer_score:
    print("congratulations you win the game")
else:
    print("you lose L better luck next time")

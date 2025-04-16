import random
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n" )
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_choice = [rock, paper, scissors]

if player_choice == "0":
    print(rock)
elif player_choice == "1":
    print(paper)
elif player_choice == "2":
    print(scissors)
else:
    print("Please Type 0, 1 or 2")
    raise SystemExit
print("Computer chose:")
computer_choice = random.choice(game_choice)
print(computer_choice)
if computer_choice == game_choice[0]:
   if player_choice == "0":
       print("It's a Draw")
   elif player_choice == "2":
       print("You Lose")
   elif player_choice == "1":
       print("You Win!")
elif computer_choice == game_choice[1]:
    if player_choice == "1":
        print("It's a Draw")
    elif player_choice == "0":
        print("You Lose")
    elif player_choice == "2":
        print("You Win!")
elif computer_choice == game_choice[2]:
    if player_choice == "2":
        print("It's a Draw")
    elif player_choice == "1":
        print("You Lose")
    elif player_choice == "0":
        print("You Win!")

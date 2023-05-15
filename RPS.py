import random
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

# rock = 0
# paper = 1
# scissors = 2
user_choice = int(input(f"What do you choose? Type {0} for Rock, {1} for Paper or {2} for Scissors. "))
computer_choice = random.randint(0, 2)
##########################################
print(f"You chose {user_choice}")
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("")
##########################################
print(f"Computer chose {computer_choice}")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
else:
    print("")
##########################################
if computer_choice == 0 and user_choice == 2:
    print("You Lose!")
    exit()
elif computer_choice == 1 and user_choice == 0:
    print("You Lose!")
    exit()
elif computer_choice == 2 and user_choice == 1:
    print("You Lose!")
    exit()
elif computer_choice == 0 and user_choice == 1:
    print("You Win!")
    exit()
elif computer_choice == 1 and user_choice == 2:
    print("You Win!")
    exit()
elif computer_choice == 2 and user_choice == 0:
    print("You Win!")
    exit()
elif computer_choice == user_choice:
    print("Draw! No Winner!")
    exit()
else:
    print("Wrong Number! You Lose!")
    exit()

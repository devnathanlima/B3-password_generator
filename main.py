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

test = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

if test == 0:
    print(rock)
elif test == 1:
    print(paper)
else:
    print(scissors)

pc = random.randint(0, 2)

print("Computer chose:")
if pc == 0:
    print(rock)
elif pc == 1:
    print(paper)
else:
    print(scissors)

if test == 0 and pc == 2:
    print("You Win!")
elif test == 0 and pc == 1:
    print("You Lose!")
elif test == 0 and pc == 0:
    print("Draw!")

if test == 1 and pc == 0:
    print("You Win!")
elif test == 1 and pc == 2:
    print("You Lose!")
elif test == 1 and pc == 1:
    print("Draw!")

if test == 2 and pc == 1:
    print("You Win!")
elif test == 2 and pc == 0:
    print("You Lose!")
elif test == 2 and pc == 2:
    print("Draw!")

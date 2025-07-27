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
PC = random.randint(0,2)
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice == 0:
    print("You Chose Rock")
    print(rock)
elif choice == 1:
    print("You Chose Paper")
    print(paper)
else:
    print("You Chose Scissors")
    print(scissors)

if PC == 0:
    print("Computer Chose Rock")
    print(rock)
elif PC == 1:
    print("Computer Chose Paper")
    print(paper)
else:
    print("Computer Chose Scissors")
    print(scissors)

if choice == PC:
    print("Match Draw")
elif choice-PC == 1 or choice-PC == -2:
    print("You Win")
else:
    print("You Lost")


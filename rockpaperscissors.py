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

#Write your code below this line 👇
import random
humanChoice = input("Digite 1 para ROCK, 2 para Paper e 3 para SCISSORS: ")
choices = [rock, paper, scissors]

humanHand = choices[int(humanChoice) - 1]

print(humanHand)

print(f"You choose{humanChoice}")
  
choise = random.choice(choices)
print(f"Computer choose{choise}")

if choise == humanHand:
  print ("Draw, nobody wins")
elif (choise == rock and humanHand == paper) or (choise == paper and humanHand == scissors) or (choise == scissors and humanHand == rock):
  print ("You Win")
else:
  print("computer Wins")
  
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

count = 0
ans = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
randi = random.randint(0,2)

rpc = [rock, paper, scissors]

print(rpc[ans])
print("Player pick")
print(rpc[randi])
print("Computer Pick")

if ans == randi:
    print("Tie! Play again")
elif ans == 0 and randi == 1:
    print("Player loss!!!!")
elif ans == 0 and randi == 2:
    print("Player wins!!!")
elif ans == 1 and randi == 0:
    print("Player wins!!!")
elif ans == 1 and randi == 2:
    print("Player loss!!!!!")
elif ans == 2 and randi == 0:
    print("Player loss!!!")
elif ans == 2 and randi == 1:
    print("Player wins!!")



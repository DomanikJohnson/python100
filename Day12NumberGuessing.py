import art
import random

print(art.logo)
print("Welcome to my guessing game!\nI I'm thinking of a number between 1-100!")
difficulty = input("Select difficulty Easy or Hard?: ")
turns = 0
if difficulty == "easy":
  turns = 10
else: 
  turns = 5

ans = random.randint(1,100)

while turns > 0:
  print(f"Turns {turns}")
  guess = int(input("Select a number: "))
  if guess < ans:
    print("Guess is too low")
  elif guess == ans:
    print("You win")
    break
  else: 
    print("Guess is too high")
  turns-=1

if turns == 0:
  print("YOU LOSE")


import random 
import art
import game_data
import replit

def most(one, two):
  if one > two:
    return "A"
  else:
    return "B"

celarr = game_data.data
randi = random.randint(0, len(celarr) - 1)
randi_next = random.randint(0, len(celarr) - 1)
ans = ""
score = 0
greatest = 0
gameover = False

print("Vs BATTLE\n")

while gameover != True:
  for cel in range(1, len(celarr)):
    winner = celarr[0]
    print(f"Compare A: {winner['name']},  {winner['description']}, from {winner['country']}")
    print(art.vs)
    print(f"Compare B: {celarr[cel]['name']},  {celarr[cel]['description']}, from {celarr[cel]['country']}")
  
    A = winner['follower_count']
    B = celarr[cel]['follower_count']
    
    greatest = most(A, B)
 
    guess  = input("Select who you think has more followers: ")

    if guess == greatest:
      score +=1
      replit.clear()
      winner = celarr[cel]
      print(f"Score is: {score}\n")

    else:
      replit.clear()
      print("You lose")
      gameover = True
      break
    
print(f"Your score is {score}")

import random

name = input("Please enter all names , seperated by a comma.")
names = name.split(", ")

randi = random.randint(0, len(names) - 1)

picked = names[randi]
output = f"{picked}! You have been chosen to pay! Thanks!!"
print(output)

from replit import clear
import art

def addBidder(name, bid):
  newBidder = {}
  newBidder['name'] = name
  newBidder['bid'] = bid

  peoplebid["bidders"].append(newBidder)

print(art.logo)
print("Welcome to the secret auction program.")

winner = ''
yon = ''

peoplebid = {
  "bidders": [],
}

while yon != 'no':
  name = input("What is your name?")
  bid = float(input("What is your bid: $"))
  addBidder(name, bid)
  yon = input("Are there any other bidders? Type 'yes' or 'no'")
  clear()

for key in peoplebid["bidders"]:
  winner = peoplebid["bidders"][0]
  most = winner['bid']

  if most < key['bid']:
      most = key['bid']
      winner =  key['name']

print(f"The winner is: {winner}")



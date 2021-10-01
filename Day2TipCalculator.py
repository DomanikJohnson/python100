print("Welcome to the tip calculator")
total = float(input("What was the total bill?"))

tip =   int(input("What percentage tip would you like to give?"))
tip_percantage = float(tip)* .01

people = int(input("How many people will split the bill"));


bill = ((total * tip_percantage) + total) / people
print("Each person will pay: {:.2f}".format(bill))
               

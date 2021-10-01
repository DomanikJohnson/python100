num = int(input("Enter your year to check for a leap year"))

if(num % 4 == 0 and num % 100 != 0):
    print("Leap year")
elif num % 4 == 0:
    if num % 100 ==  0 and num % 400  == 0:
        print("Leap year")
else:
    print("Not a leap year")



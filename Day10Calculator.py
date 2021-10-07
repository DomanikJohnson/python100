import art
import replit

def add(firstnum = 0, nextnum = 0, morenum = 0):
  ans = firstnum + nextnum + morenum
  return ans

def sub(firstnum = 0, nextnum = 0, morenum = 0):
  ans = firstnum - nextnum - morenum
  return ans

def mul(firstnum = 0, nextnum = 0, morenum = 0):
  ans = firstnum * nextnum
  return ans

def div(firstnum = 0, nextnum = 0, morenum = 0):
  ans = firstnum / nextnum
  return ans

def maincall(oper):
  ans = 0
  if oper == "+":
    ans = add(firstnum, nextnum)
    return ans
  if oper == "-":
    ans = sub(firstnum, nextnum)
    return ans
  if oper == "*":
    ans = mul(firstnum, nextnum)
    return ans 
  if oper == "/":
    ans = div(firstnum, nextnum)
    return ans

usrflag = False
glb = 0
print(art.logo)
while usrflag != True:
 
  firstnum = float(input("Enter the first number: "))
  op = input("+\n-\n*\n\\\nPick an operation?: ")
  nextnum = float(input("What is the next num: "))
  glb = maincall(op)
  print(f"{firstnum} {op} {nextnum} = {glb}")

  nextgo = input(f"Type 'y' to continue calculating with {maincall(op)}, or type 'n' to type a new calculation")
  if nextgo == 'y':
      while nextgo != 'n':
        op = input("+\n-\n*\n\\\n Pick an operation?: ")
        nextnum = float(input("What is the next num: "))
        n = glb
        glb = add(glb, nextnum)
        print(f"{n} {op} {nextnum} = {glb}")
        nextgo = input(f"Type 'y' to continue calculating with {maincall(op)}, or type 'n' to type a new calculation")
      replit.clear()





heights = input("What are the classes heights").split()
total = 0
for hei in heights:
  total+=int(hei)

ans = round(total/len(heights))
print(ans)
 

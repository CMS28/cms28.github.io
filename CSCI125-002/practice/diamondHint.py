# the upper 
for i in range(9):
    for j in range(9-i):
        print(" ",end="")
    for j in range(9-i,9+i+1):
        print("*",end="")
    print()

for i in range(9,-1,-1):
    for j in range(9-i):
        print(" ",end="")
    for j in range(9-i,9+i+1):
        print("*",end="")
    print()
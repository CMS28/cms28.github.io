# read line by line
f = open("keycodes.txt","r")

# read the first line
keycodelist =[]
'''
newcode = f.readline()
while newcode != "":
    newcode = f.readline()
    keycodelist.append(newcode)
'''
for newcode in f:
    keycodelist.append(newcode[:-1])

#print
print(keycodelist)
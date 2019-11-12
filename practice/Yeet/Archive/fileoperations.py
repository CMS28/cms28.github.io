'''
f = open("list.py", "r")
t = open("write.png", "w")
content = "content to write"

t.write(f.read())

f.close()
t.close()
'''
'''
f = open("my.png", "w")
mylist=["good","\n","bad","\n", "best"]
for i in mylist:
    task = i
    f.write(i)
print("done")
'''
f=open("keycodes.txt", "r")
keycodelist =[]
'''
for i in range(154):
    newcode=f.readline()
    keycodelist.append(newcode)
'''
for newcode in f:
    keycodelist.append(newcode[:-1])

usercode = input("Enter pin")
if usercode in keycodelist:
    print("HoofuckingRay")
else:
    print("BooFuckingHoo")
'''
print(keycodelist)
'''
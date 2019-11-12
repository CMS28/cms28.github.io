#find the lowest score of the list
def lowest(scorelist):
    smallsofar = scorelist[0]
    for num in scorelist:
        if num< smallsofar:
            smallsofar = num
        else:
            pass
    return smallsofar


# find the total, drop the lowest
def total(scorelist):
    sum = 0
    for i in scorelist:
        sum = sum + i
    drop = (sum - lowest(scorelist))/(len(scorelist)-1)
    return drop
#read the data from the files
for b in range(1,11):
    mylist=[]
    if b==1:
        f = open('score1.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    elif b==2:
        f = open('score2.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    elif b==3:
        f = open('score3.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    elif b==4:
        f = open('score4.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    elif b==5:
        f = open('score5.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    elif b==6:
        f = open('score6.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    elif b==7:
        f = open('score7.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    elif b==8:
        f = open('score8.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    elif b==9:
        f = open('score9.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    elif b==10:
        f = open('score10.txt','r')
        for lines in f:
            cleardata = int(lines[:-1])
            mylist.append(cleardata)
            print(mylist)
    print(f'The average score for this list is {total(mylist)}')
    print()
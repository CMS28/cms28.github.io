
# find the lowest score of the list- input/ output is lowest
def lowest(scorelist):
    smallestSofar = scorelist[0]
    for num in scorelist:
        if num < smallestSofar:
            smallestSofar = num
    return smallestSofar

# test it -- done

# find the total, drop the lowest, do average
def specialA(scorelist):
    sum = 0
    for num in scorelist:
        sum = sum + num
    ans =( sum - lowest(scorelist))/(len(scorelist)-1)
    return ans

# read the data from files
f = open('score1.txt','r')
# the data need be clean up mylist = list(f)
mylist=[]
for lines in f:
    cleardata = int(lines[:-1])
    mylist.append(cleardata)
#test it - done
# print(mylist)

print(f'The average score for score1.txt is {specialA(mylist)}')

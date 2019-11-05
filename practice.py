'''
#print evens
for i in range(2,21,2):
    print(i)
'''
'''
#print num divisible by 3
for i in range(1,20):
    if i%3==0:
        print(i)
    else:
        pass
'''
'''
#square of each odd number
for i in range(1,20,2):
    ans=i**2
    print(ans)
'''
'''
#     1
#    121
#   12321
#  1234321
# 123454321

for i in range(1,6):
    if i == 1:
        print(" "," "," "," ",i,)
    elif i == 2:
        print(" "," "," ",1,i,1)
    elif i == 3:
        print(" "," ",1,2,i,2,1)
    elif i == 4:
        print(" ",1,2,3,i,3,2,1)
    else:
        print(1,2,3,4,i,4,3,2,1)
    print()
'''
'''
#multiplication table
for i in range(1,10):
    for j in range(1,10):
        ans = i*j
        print(f"{j}*{i}={ans}", end=" ")
    print()
'''
'''
num = 1/i
sum = 0
for i in range(2,100001,2):
    sum = sum + num
    print(sum)
'''
'''
for i in range(5):
    for j in range(1,2+i):
        print("*", end=" ")
    print()
'''

for loan in range(100000, 1000001, 100000):
    print(f"{loan}", end=" \t |\t")
    for rate in [3.5, 4.0, 4.25, 6.0]:
        mrate =rate/1200
        payment = loan * mrate/(1-(1+mrate)**(-360))
        print(f'{payment:.2f}', end=" ")
    print()
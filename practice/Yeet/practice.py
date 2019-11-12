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

#     1
#    121
#   12321
#  1234321
# 123454321

'''
i=1
for j in range(1,6):
    n=10**j
    j=i**2
    print(j)
    i=i+n
print()
'''

#multiplication table
'''
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

'''
for loan in range(100000, 1000001, 100000):
    print(f"{loan}", end=" \t |\t")
    for rate in [3.5, 4.0, 4.25, 6.0]:
        mrate =rate/1200
        payment = loan * mrate/(1-(1+mrate)**(-360))
        print(f'{payment:.2f}', end=" ")
    print()
'''


#Function Revisit
'''
def sqr(x):
    return x*x
t=False
while t==False:
    x=input("What is the value of x? ")

'''
'''
#sum and factorial
sum = 1
def factorial(n):
    prod = 1
    for num in range(1,n+1):
        prod = prod * num
    return prod

#sum
for num in range(1,101):
    sum = sum + 1/factorial(num)
    print(sum)
'''

def Fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(8))
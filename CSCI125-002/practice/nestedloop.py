'''
for i in range(5):  
    for j in range(7):
        print("*",end=" ")
    print("\n--------------------------")

for i in range(1,6):
    for j in range(1,4):
        ans = i *j
        print(f"{j}x{i}={ans}", end=" ")
    print()
'''
'''
for i in range(6):
    for j in range(6-i):
        if j==6-i-1:
            print(f'{i+1}')
        else:
            print(".", end=" ")
    print()
'''

for loan in range(100000, 1000001, 100000):
    print(f"{loan}", end="  \t |\t")
    for rate in [3.5, 4.0,4.25,6.0]:
        mrate =rate /1200
        payment = loan * mrate/(1-(1+mrate)**(-360))
        print(f'{payment:.2f}', end=" ")
    print()


#    1+1+1/2!+1/3!+…+1/100!     
#    sum --done  2!, 3!, 6!..... ?

def factorial(N):
    # try a simple case 10!--N!
    prod = 1
    for num in range(1,N+1):
        prod = prod * num
    return prod

# test function -- done 
print(factorial(3))  
# sum 
sum = 1
for num in range(1,101):
    sum = sum + 1/factorial(num)
print(sum)
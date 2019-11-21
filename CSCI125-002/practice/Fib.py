def Fib(n):
    #base case
    if n==0:
        return 2
    elif n ==1:
        return 3
    else:
        return Fib(n-1)+Fib(n-2)
#test function
print(Fib(8))


def recur_sum(n):
    #base case
    if n == 1:
        return  ### finsh
    else:
        return recur_sum(n-1)+n
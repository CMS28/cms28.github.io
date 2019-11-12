def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
        print(f"multiply the {i}")
    return ans
print(factorial(5))


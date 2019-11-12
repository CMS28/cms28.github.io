sum = 0
for i in range(1,100):
    if (i%2)==0:
        print("skip")
    else:
        sum = sum + i
    print(f"add {i}")
print(f"the sum is {sum}")
evens1 = [2, 1, 2, 3, 4]
evens2 = [2, 2, 0]
evens3 = [1, 3, 5]
for num in evens1:
    if num % 2 == 0:
        count_even1 =+1
    else:
        print()

for num in evens2:
    if num % 2 == 0:
        count_even2 +=1
    else:
        print()

for num in evens3:
    if num % 2 == 0:
        count_even3 +=1
    else:
        print()


print("Even numbers in the list", count_even1)
print("Even numbers in the list", count_even2)
print("Even numbers in the list", count_even3)
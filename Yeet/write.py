def count_even(mylist ):
    numeven = 0
    for num in mylist:
        if num%2==0:
            numeven +=1
        else:
            pass
    return numeven
print(coutn_even([2, 2, 0]))
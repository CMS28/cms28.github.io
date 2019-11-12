limit=float(input("What was the speed limit?"))
speed=float(input("How fast was the person going?"))
difference=int(speed)-int(limit)
if dif < 5:
    cost="$0"
elif dif > 5 and < 10:
    cost="$25"
elif dif >10 and < 14:
    cost="100"
elif dif > 14 and < 19:
    cost="$125"
elif  dif > 19 and < 24:
    cost="$150"
elif dif >24 and < 34:
    cost="$500"
else:
    pass
print(f"The cost of the ticket is {cost}.")

height= float(input("height "))
weight= float(input("weight "))
bmi=703*weight/(height**2)
if bmi<18.5:
    message="You are underweight."
elif bmi<25:
    message="You are normal."
elif bmi<30:
    message="You are overweight."
else:
    pass

print(f"{message}")

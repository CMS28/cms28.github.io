grade=input("What is the student's grade?")
if grade>89:
    letter="A"
elif grade >= 79:
    letter="B"
elif grade>69:
    letter="C"
else:
    letter="F"
print(f"The student's letter grade is {letter}.")

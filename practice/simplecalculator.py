
# need input like 3 + 4
print("Please type the expressinon as 3 + 4")
expression = input()
num1, op, num2 = experssion.split()
# they are string type!!!
a = float(num1)
b = float(num2)

# ready for process
ans = 0 
if op == "+":
    ans = a + b
elif op =="-":
    ans = a - b


# output 
print(f'{a} {op} {b} is {ans}')
process = False
while process == False:
    expression = input()
    num1, op, num2 = expression.split()
    a = float(num1)
    b = float(num2)
    ans = 0
    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    elif op == "/":
        ans = a / b
    elif op == "*":
        ans = a * b
    elif op == "**":
        ans = a ** b
    elif op == "%":
        ans = a % b
    else:
        break
    print(f"{a} {op} {b} is {ans}")
    process = False
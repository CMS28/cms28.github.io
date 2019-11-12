process = False
while process == False:
    salary = int(input("What is the employee's salary?"))
    onjob = int(input("'How long have they been working here?"))
    if salary < 40000:
        if onjob > 5:
            print("Qualified")
        else:
            print("Not Qualified")
    elif salary <60000:
        if onjob > 25:
            print("Qualified")
        else:
            print("Not Qualified")
    else:
        print("Not Qualified")
    process = False
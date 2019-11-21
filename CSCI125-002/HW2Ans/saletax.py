# Exercise 2

# Program Created By Doryan Broadwater

# Write a python program that calculates and displays the county and state sales tax on a purchase, assume The combined sales tax rate for Aiken Country, SC is 8%. 

#input
print(" This Program Calculates How Much Your Item Will Be After Taxes In SC ")

purchase = input("       How Much Was Your Purchase Before Tax? (in dollars) ")

# process (float is used instead of int so change can be added)
salestax = float(purchase) * .08

overall = float(purchase) + float(salestax)

# output
print("             The sales tax of your purchase is " + "$" + str(salestax) )
print("")
print("          All Together You Will Be Paying " + "$" + str(overall) + " dollars " )
print("")

# The words are spaced out in order to give a better look in terminal when ran. 

#finished , 8 lines of code to run (extra to give aesthetic)
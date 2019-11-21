# Gas Mileage by Adam Buchanan

#Input
gallon = input('How many gallons of gas can yourcar hold? ')
miles = input('How many miles can your car be driven on a full tank of gas? ')
gasPrice = float(2.720)
#Process
MPG = float(miles) / float(gallon)
pricePerMile = float(gasPrice) / float(MPG)

#Output
print(f'Your car gets {MPG:.2f} miles to the gallon and the gas costs ${pricePerMile:.2f} per mile.')
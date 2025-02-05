#input we neend from the user
# total rent
# total food ordered 
# charge per unit
# persons living in room

## output
# total amount you have to pay is 

rent = int(input("Enter your hostal/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
charge_per_unit = int(input("Enter the charge per unit = "))
electricity_spend = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend*charge_per_unit
output = (food+rent+total_bill)//persons
print("Each person will have to pay =", output)